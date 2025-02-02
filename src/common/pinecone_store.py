from pinecone import Pinecone, ServerlessSpec
import os
import hashlib
from typing import List, Dict, Any

class PineconeStore():
    def __init__(self, index_name: str, model: str = "multilingual-e5-large"):
        self.model = model
        api_key = "pcsk_6eJuMV_NkGGMeP15ALnvPWdBVozoQoa5Qf92S8xXiCPat8C8mGjcxNoFSGAhY7cWaVZmqS"  # Use environment variable for security
        self.pc = Pinecone(api_key=api_key)
        self.index_name = index_name
        
        if not self.pc.has_index(index_name):
            self.pc.create_index(
                name=index_name,
                dimension=1024,
                metric='cosine',
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        
        index_description = self.pc.describe_index(index_name)
        index_host = index_description['host']
        self.index = self.pc.Index(host=index_host)

    def add_embedding(
            self, video_title: str, chunks: List[str], metadata: List[Dict[str, Any]] = None, namespace: str = ""
        ) -> bool:
        """
        Add text chunks along with a video title embedding to the Pinecone index.
        
        Args:
            video_title (str): The title of the video to be embedded.
            chunks (List[str]): List of text chunks to embed and store.
            metadata (List[Dict], optional): List of metadata for each chunk.
            namespace (str, optional): Namespace for the vectors.
        
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Generate embedding for video title (Fix: Use "query" instead of "title")
            video_embedding = self.pc.inference.embed(
                model=self.model,
                inputs=[video_title],
                parameters={"input_type": "query"}  # <-- Fix: Change from "title" to "query"
            )[0]["values"]

            # Store video title embedding separately
            video_id = hashlib.sha256(video_title.encode()).hexdigest()
            self.index.upsert(
                vectors=[{
                    "id": video_id,
                    "values": video_embedding,
                    "metadata": {"title": video_title}
                }],
                namespace=namespace
            )

            # Process text chunks in batches of 96
            batch_size = 96
            for i in range(0, len(chunks), batch_size):
                batch_chunks = chunks[i:i + batch_size]
                batch_metadata = metadata[i:i + batch_size] if metadata else None

                # Generate embeddings for text chunks (Fix: Use "passage" instead of "title")
                chunk_embeddings = self.pc.inference.embed(
                    model=self.model,
                    inputs=batch_chunks,
                    parameters={"input_type": "passage"}  # <-- Fix: Change from "title" to "passage"
                )

                # Prepare records for upsertion
                records = []
                for j, (chunk, embedding) in enumerate(zip(batch_chunks, chunk_embeddings)):
                    chunk_id = hashlib.sha256(chunk.encode()).hexdigest()
                    record = {
                        "id": chunk_id,
                        "values": embedding['values'],
                        "metadata": batch_metadata[j] if batch_metadata else {"text": chunk, "video_title": video_title}
                    }
                    records.append(record)

                # Upsert current batch to index
                self.index.upsert(vectors=records, namespace=namespace)

            return True
        except Exception as e:
            print(f"Error adding chunks with video title: {str(e)}")
            return False


    def query_embedding(self, video_title: str, top_k: int = 10, namespace: str = "") -> List[Dict]:
        """
        Query the index using a video title to find related videos.
        
        Args:
            video_title (str): The title of the video to search for.
            top_k (int): Number of related videos to return.
            namespace (str, optional): Namespace to search in.
            
        Returns:
            List[Dict]: List of matching videos with scores and metadata.
        """
        try:
            # Generate embedding for video title query (Fix: Use "query" instead of "title")
            title_embedding = self.pc.inference.embed(
                model=self.model,
                inputs=[video_title],
                parameters={"input_type": "query"}  # <-- Fix: Change from "title" to "query"
            )

            # Query the index
            results = self.index.query(
                namespace=namespace,
                vector=title_embedding[0]['values'],
                top_k=top_k,
                include_metadata=True
            )

            # Extract video titles from results
            related_videos = []
            for match in results.matches:
                if "title" in match.metadata:
                    related_videos.append({
                        "title": match.metadata["title"],
                        "score": match.score,
                        "metadata": match.metadata
                    })

            return related_videos
        except Exception as e:
            print(f"Error querying video title: {str(e)}")
            return []


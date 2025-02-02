from pinecone import Pinecone, ServerlessSpec
import os
import hashlib
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")


class PineconeStore():
    def __init__(self, index_name: str, model: str = "multilingual-e5-large"):
        self.model = model
        self.pc = Pinecone(api_key=API_KEY)
        self.index_name = index_name
        self.num = 5

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
        self, video_title: str, video_id: int, namespace: str = ""
    ) -> bool:
        """
        Add text chunks along with a video title embedding to the Pinecone index.

        Args:
            video_title (str): The title of the video to be embedded.
            chunks (List[str]): List of text chunks to embed and store.
            metadata (List[Dict], optional): List of metadata for each chunk (must include "age").
            namespace (str, optional): Namespace for the vectors.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Generate embedding for video title
            video_embedding = self.pc.inference.embed(
                model=self.model,
                inputs=[video_title],
                # Use "query" for video titles
                parameters={"input_type": "query"}
            )[0]["values"]

            # Ensure metadata contains age, default to None if not provided
            # video_age = metadata[0].get("age") if metadata and "age" in metadata[0] else None

            # Store video title embedding separately
            video_title_id = hashlib.sha256(video_title.encode()).hexdigest()
            self.index.upsert(
                vectors=[{
                    "id": video_title_id,
                    "values": video_embedding,
                    # Add age metadata
                    "metadata": {"title": video_title, "age": video_id}
                }],
                namespace=namespace
            )

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
                # <-- Fix: Change from "title" to "query"
                parameters={"input_type": "query"}
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
                        "metadata": match.metadata,
                        "id": match.metadata["age"]
                    })

            return related_videos
        except Exception as e:
            print(f"Error querying video title: {str(e)}")
            return []

import time
from pinecone_store import PineconeStore  # Assuming your class is in pinecone_store.py

def test_pinecone_video_recommendations():
    index_name = "test-video-index"
    pinecone_store = PineconeStore(index_name=index_name)
    
    # Define video titles with some related topics
    videos = [
        ("Linear Algebra Basics", ["Vectors and Matrices", "Eigenvalues and Eigenvectors"]),
        ("Advanced Linear Algebra", ["Singular Value Decomposition", "Matrix Factorization"]),
        ("Introduction to Calculus", ["Limits and Derivatives", "Integrals"]),
        ("Multivariable Calculus", ["Partial Derivatives", "Gradient and Hessian"]),
        ("Machine Learning Foundations", ["Supervised Learning", "Unsupervised Learning"]),
        ("Deep Learning Explained", ["Neural Networks", "Backpropagation"]),
        ("Computer Vision Basics", ["Image Processing", "Object Detection"]),
        ("Natural Language Processing", ["Text Classification", "Word Embeddings"]),
        ("Reinforcement Learning", ["Markov Decision Processes", "Policy Gradients"]),
        ("Optimization Techniques", ["Gradient Descent", "Convex Optimization"])
    ]
    
    # Add videos to Pinecone
    for title, chunks in videos:
        success = pinecone_store.add_embedding(video_title=title, chunks=chunks)
        if success:
            print(f"Successfully added video: {title}")
    
    # Wait for index update
    time.sleep(5)
    
    # Query Pinecone with a title
    query_title = "Linear Algebra"
    print(f"Querying Pinecone for similar videos to: {query_title}")
    results = pinecone_store.query_embedding(query_title, top_k=5)
    
    # Display results
    print("Top recommended videos:")
    for res in results:
        print(f"- {res['title']} (score: {res['score']:.4f})")
    
    # Check if at least one relevant video is returned
    assert any("Linear Algebra" in res['title'] for res in results), "No relevant videos found!"
    print("Test passed: Relevant videos were found.")

if __name__ == "__main__":
    test_pinecone_video_recommendations()

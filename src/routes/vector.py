from fastapi import APIRouter
from common.pinecone_store import PineconeStore

router = APIRouter()

INDEX_NAME = "test-video-index"
pinecone = PineconeStore(INDEX_NAME)


@router.get("/search")
def vector_search(query: str):
    results = pinecone.query_embedding(query)
    return {
        "results": results
    }

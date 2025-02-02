from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from common.pinecone_store import PineconeStore
from common.db import find_ids
import time

router = APIRouter()

INDEX_NAME = "test-video-index"
pinecone = PineconeStore(INDEX_NAME)


@router.get("/search")
def vector_search(query: str):
    results = pinecone.query_embedding(query)
    return find_ids(str(res["id"]) for res in results)

# @router.post("/add")
# def add_vector():
#     t = time.time()
#     return pinecone.add_embedding(str(t), int(t))

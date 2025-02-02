import sys
import os
from celery import Celery
from routes import video
from video_storage.storage import run_video_pipeline
import asyncio
import time
from common.pinecone_store import PineconeStore
from react_orchestrator import ReactOrchestrator


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "src")))


INDEX_NAME = "test-video-index"
pinecone = PineconeStore(INDEX_NAME)


app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


# video_data is a dictionary
# requires "video_path", "id" and "image_path" keys
# you can inlcude any other keys as well
@app.task
def start_vid_pipeline(prompt: str):
    from video_orchestrator import VideoOrchestrator
    video_id = str(time.time())
    data = asyncio.run(
        asyncio.gather(
            VideoOrchestrator(prompt).generate_and_render_video(),
            ReactOrchestrator(prompt).generate_and_return_components()
        )
    )

    print("DATA IS HERE:", data)
    video_data = data[0]
    react_code = data[1]

    if not video_data or "video_path" not in video_data or "image_path" not in video_data:
        return {
            "status": "FAILED",
            "message": "Failed to generate video",
        }

    react_code = asyncio.run()

    if not react_code and "react_code" not in react_code:
        return {
            "status": "FAILED",
            "message": "Failed to generate react code",
        }

    video_data["react_code"] = react_code["react_code"]

    video_data["id"] = video_id
    time.sleep(5)
    data = run_video_pipeline(video_data)
    pinecone.add_embedding(video_data["video_title"], video_id)

    return {
        "status": "DONE",
        "data": {**video_data, **data},
    }

import sys
import os
from celery import Celery
from video_storage.storage import run_video_pipeline
import asyncio
import time


sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "src")))


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
    video_data = asyncio.run(VideoOrchestrator(
        prompt).generate_and_render_video())

    print(video_data)

    if not video_data or "video_path" not in video_data or "image_path" not in video_data:
        return {
            "status": "FAILED",
            "message": "Failed to generate video",
        }

    video_data["id"] = video_id
    time.sleep(5)
    data = run_video_pipeline(video_data)
    return {
        "status": "DONE",
        "data": data,
    }

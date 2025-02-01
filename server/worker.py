from celery import Celery
from video_storage.storage import run_video_pipeline
import time

app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


# video_data is a dictionary
# requires "video_path", "id" and "image_path" keys
# you can inlcude any other keys as well
@app.task
def start_vid_pipeline(video_data):
    print("Starting video pipeline")
    print(video_data)
    time.sleep(5)
    data = run_video_pipeline(video_data)
    return {
        "status": "DONE",
        "data": data,
    }

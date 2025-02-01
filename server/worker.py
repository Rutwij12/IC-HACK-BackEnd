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
def start_vid_pipeline():
    print("Starting video pipeline")
    # call claude here
    # return dictionary with keys: "video_path", "id" and "image_path"
    # and any other keys you want
    video_data = {
        "video_path": "../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4",
        "id": "test1",
        "image_path": "/home/jay/Repos/IC-HACK-BackEnd/media/images/tree-736885_1280.jpg",
    }
    time.sleep(5)
    data = run_video_pipeline(video_data)
    return {
        "status": "DONE",
        "data": data,
    }

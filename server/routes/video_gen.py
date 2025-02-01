from fastapi import APIRouter
from models import GenVideoInput
from worker import start_vid_pipeline
from celery.result import AsyncResult

router = APIRouter()


@router.post("/gen_video")
async def gen_video(data: GenVideoInput):
    prompt = data.prompt

    # call claude here
    # return dictionary with keys: "video_path", "id" and "image_path"
    # and any other keys you want
    video_data = {
        "video_path": "../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4",
        "id": "test1",
        "image_path": "/home/jay/Repos/IC-HACK-BackEnd/media/images/tree-736885_1280.jpg",
    }

    task = start_vid_pipeline.delay(video_data)
    return {"task_id": task.id}


@router.get("/video_status")
async def get_vid_status(task_id: str):
    print(task_id)
    status = AsyncResult(task_id)
    return {
        "status": status.state,
        "result": status.result,
    }

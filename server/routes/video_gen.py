from fastapi import APIRouter
from models import GenVideoInput
from worker import start_vid_pipeline
from celery.result import AsyncResult

router = APIRouter()


@router.post("/gen_video")
async def gen_video(data: GenVideoInput):
    prompt = data.prompt

    task = start_vid_pipeline.delay()
    return {"task_id": task.id}


@router.get("/video_status")
async def get_vid_status(task_id: str):
    print(task_id)
    status = AsyncResult(task_id)
    return {
        "status": status.state,
        "result": status.result,
    }

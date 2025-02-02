from fastapi import APIRouter

router = APIRouter()


@router.get("/video")
def get_video(video_id: str):
    pass

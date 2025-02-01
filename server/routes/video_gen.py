from fastapi import APIRouter
from models import GenVideoInput
from video_storage.storage import upload_video, store_video_metadata

router = APIRouter()

ERROR = {
    "url": None,
    "message": "",
}

@router.post("/gen_video")
def gen_video(data : GenVideoInput):
    prompt = data.prompt

    # call claude here - return video path, id, metadata key : args
    video_data = {
        "video_path": "../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4",
        "video_id": "test1",
    }

    if not video_data or "video_path" not in video_data or "video_id" not in video_data:
        return {**ERROR, "message": "Failed to generate video"}
    # upload the video

    url = upload_video(video_data['video_path'], video_data['video_id'])
    if not url:
        return {**ERROR, "message": "Failed to upload video"}

    # store the video metadata
    if not store_video_metadata(url, **video_data):
        return {**ERROR, "message": "Failed to store video metadata"}

    # send video link
    return {
        "url": url
    }





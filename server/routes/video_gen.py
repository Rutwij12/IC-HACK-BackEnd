from fastapi import APIRouter
from models import GenVideoInput
from video_storage.storage import upload_video, store_video_metadata, upload_image

router = APIRouter()

ERROR = {
    "url": None,
    "message": "",
}


@router.post("/gen_video")
def gen_video(data: GenVideoInput):
    prompt = data.prompt

    # call claude here - return video path, id, metadata key : args
    video_data = {
        "video_path": "../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4",
        "id": "test1",
        "image_path": "/home/jay/Repos/IC-HACK-BackEnd/media/images/tree-736885_1280.jpg",
    }

    if not video_data or "video_path" not in video_data or "id" not in video_data:
        return {**ERROR, "message": "Failed to generate video"}
    # upload the video

    video_url = upload_video(video_data['video_path'], video_data['id'])
    if not video_url:
        return {**ERROR, "message": "Failed to upload video"}
    image_url = upload_image(video_data['image_path'], video_data['id'])

    # store the video metadata
    if not store_video_metadata(video_url, image_url, **video_data):
        return {**ERROR, "message": "Failed to store video metadata"}

    # send video link
    return {
        "video_url": video_url,
        "image_url": image_url,
    }

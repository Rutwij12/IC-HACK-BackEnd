from fastapi import APIRouter
from models import VideoGen
from video_storage.storage import upload_video, store_video_metadata

router = APIRouter()

@router.post("/gen_video")
def upload_video(data : VideoGen):
    prompt = data.prompt

    # call claude here - return video path, id, metadata key : args
    video_data = "", "" 


    if not video_data: #Keys like "Name"
        return {"message": "Failed to generate video", "url": None}
    # upload the video

    url = upload_video(video_data['video_path'], video_data['video_id'])

    # store the video metadata
    store_video_metadata(url, **video_data)

    # send video link
    return {
        "url": url
    }





from fastapi import APIRouter
import boto3
router = APIRouter()


table = boto3.resource('dynamodb').Table("Videos")
s3 = boto3.client('s3')


@router.get("/videos")
def get_video(video_id: str):
    print(video_id)
    response = table.get_item(Key={"id": video_id})
    if "Item" not in response:
        return {"message": "Video not found"}
    return response["Item"]

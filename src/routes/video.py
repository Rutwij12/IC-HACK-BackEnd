from fastapi import APIRouter
import boto3
router = APIRouter()

table = boto3.resource('dynamodb').Table("video")
s3 = boto3.client('s3')

@router.get("/video")
def get_video(video_id: str):
    response = table.get_item(Key={"id": video_id})
    if "Item" not in response:
        return {"message": "Video not found"}
    return response["Item"]
    

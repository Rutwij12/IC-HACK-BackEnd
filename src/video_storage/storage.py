import boto3
from time import time
import os

BUCKET_NAME = "ic-hack"
TEST_VIDEO_PATH = "../../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4"

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
VIDEO_TABLE = os.getenv("VIDEO_TABLE")
table = db.Table(VIDEO_TABLE)

ERROR = {
    "url": None,
    "message": "",
}


def run_video_pipeline(video_data):
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


def upload_video(video_path, video_id) -> str | None:
    try:
        print()
        if os.path.exists(video_path):
            object_name = f"videos/{video_id}.mp4"
            print(object_name)
            s3.upload_file(video_path, BUCKET_NAME, object_name)
            public_url = f"https://{
                BUCKET_NAME}.s3.eu-west-2.amazonaws.com/{object_name}"
            return public_url
        else:
            print("File does not exist")
    except Exception as e:
        print(e)
    return None


def upload_image(image_path, id) -> str | None:
    try:
        if os.path.exists(image_path):
            object_name = f"images/{id}.png"
            s3.upload_file(image_path, BUCKET_NAME, object_name)
            public_url = f"https://{
                BUCKET_NAME}.s3.eu-west-2.amazonaws.com/{object_name}"
            return public_url
    except Exception as e:
        print(e)
    return None


def store_video_metadata(video_url, image_url, id, **kargs):
    try:
        res = table.put_item(Item={
            "id": id,
            **kargs,
            "video_url": video_url,
            "image_url": image_url,
            "created_at": int(time()),
        })
        return res.get("ResponseMetadata").get("HTTPStatusCode") == 200
    except Exception as e:
        print(e)
    return False


if __name__ == "__main__":
    video_id = "test1"
    url = upload_video(TEST_VIDEO_PATH, video_id)
    store_video_metadata(
        url, video_id, **{"Name": "Test Video", "Prompt": "Test Prompt"})
    print(url)

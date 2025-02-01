import boto3
from time import time
from dotenv import load_dotenv
import os

load_dotenv()

BUCKET_NAME = "ic-hack"
TEST_VIDEO_PATH = "../../media/videos/scene_4_temp_code/480p15/LinearTransformationProperties.mp4"

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
VIDEO_TABLE = os.getenv("VIDEO_TABLE")
print(VIDEO_TABLE)
table = db.Table(VIDEO_TABLE)


def upload_video(video_path, video_id) -> str | None:
    try:
        print(os.getcwd())
        if os.path.exists(video_path):
            object_name = f"videos/{video_id}.mp4"
            s3.upload_file(video_path, BUCKET_NAME, object_name)
            public_url = f"https://{BUCKET_NAME}.s3.eu-west-2.amazonaws.com/{object_name}"
            return public_url
    except Exception as e:
        print(e)
    return None

def store_video_metadata(url, video_id, **kargs):
    try:
        res = table.put_item(Item={
            "id": video_id,
            **kargs,
            "url": url,
            "created_at": int(time()),
        })
        return res.get("ResponseMetadata").get("HTTPStatusCode") == 200
    except Exception as e:
        print(e)
    return False


if __name__ == "__main__":
    video_id = "test1"
    url = upload_video(TEST_VIDEO_PATH, video_id)
    store_video_metadata(url, video_id, **{"Name": "Test Video", "Prompt": "Test Prompt"})
    print(url)
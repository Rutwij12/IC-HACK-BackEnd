import boto3
from boto3.dynamodb.conditions import Key
import os

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
VIDEO_TABLE = os.getenv("VIDEO_TABLE")
table = db.Table(VIDEO_TABLE)


def find_ids(ids):
    results = []
    for id_val in ids:
        res = table.query(KeyConditionExpression=Key('id').eq(id_val))
        print(res)
        results += res.get("Items", [])

    return results

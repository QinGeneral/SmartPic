# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import json
import time
import os

secret_id = "xxx"
secret_key = "xxx"
region = "xxx"
bucket = "xxx"


def write_content_to_file(file_name, content):
    file_ob = open(file_name, 'w')
    file_ob.write(content)
    file_ob.close()


def read_file_content(file_name):
    file_ob = open(file_name, 'r')
    content = file_ob.read()
    file_ob.close()
    return content


def uploadPic(key, file_name, client):
    response = client.put_object_from_local_file(
        Bucket=bucket,
        LocalFilePath=file_name,
        Key=key,
        EnableMD5=False
    )


def downloadPic(key, file_name, client):
    response = client.get_object(
        Bucket=bucket,
        Key=key,
    )
    response['Body'].get_stream_to_file(file_name)


def main():
    global secret_id, secret_key, region, bucket

    config_json = read_file_content("config.txt")
    config = json.loads(config_json)

    secret_id = config["secret_id"]
    secret_key = config["secret_key"]
    region = config["region"]
    bucket = config["bucket"]

    cos_config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

    client = CosS3Client(cos_config)
    file_name = sys.argv[1]

    last_slash_index = file_name.rfind('/')
    key = str(time.time())
    if last_slash_index == -1:
        key = key + file_name
    else:
        key = key + file_name[last_slash_index + 1:]

    uploadPic(key, file_name, client)
    result = config["blog_prefix"] + "/" + key
    sys.stdout.write(result)


if __name__ == "__main__":
    main()
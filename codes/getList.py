# -*- coding=utf-8
import sys
import logging
import json
import time
import os

def write_content_to_file(file_name, content):
    file_ob = open(file_name, 'w')
    file_ob.write(content)
    file_ob.close()


def read_file_content(file_name):
    file_ob = open(file_name, 'r')
    content = file_ob.read()
    file_ob.close()
    return content


def main():
    result = {"items": []}

    content = read_file_content('history.log')
    if len(content) == 0:
        result["items"].append({
            "title":'已上传 0 张图片',
            "subtitle": "移动到指定图片，按下 Cmd + Y 可查看图片",
            "arg": "noPic",
            "icon": "5E995555-07AF-4314-B882-C89ABAF2ED7A.png"})
        print(json.dumps(result))
        return -1
    answers = content.split("\n")

    if not answers:
        result["items"].append({
            "title":'已上传 0 张图片',
            "subtitle": "移动到指定图片，按下 Cmd + Y 可查看图片",
            "arg": "noPic",
            "icon": "5E995555-07AF-4314-B882-C89ABAF2ED7A.png"})
        print(json.dumps(result))
        return -1

    result["items"].append({
            "title":'已上传 ' + str(len(answers) / 2) + ' 张图片，移动后 Cmd + Y 可查看图片',
            "subtitle": "移动后 Enter 可复制对于图片链接",
            "arg": "noPic",
            "icon": "5E995555-07AF-4314-B882-C89ABAF2ED7A.png"})
    i = 0
    while(i < len(answers) - 1):
        result["items"].append({
            "title": answers[i],
            "subtitle": answers[i + 1],
            "arg": answers[i + 1],
            "autocomplete": answers[i],
            "icon": "5E995555-07AF-4314-B882-C89ABAF2ED7A.png"
        })
        i = i + 2
    print(json.dumps(result))


if __name__ == '__main__':
    main()

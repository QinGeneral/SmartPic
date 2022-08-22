# -*- coding=utf-8
import sys
import json


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
    config_json = read_file_content("config.txt")
    try:
        config = json.loads(config_json)
    except ValueError:
        sys.stdout.write("no")

    if ('secret_id' in config) & ('secret_key' in config) & ('region' in config) & ('bucket' in config) & ('blog_prefix' in config) & (config['secret_id'] != 'xxxxxx') & (config['secret_key'] != 'xxxxxx') & (config['region'] != 'xxxxxx') & (config['bucket'] != 'xxxxxx') & (config['blog_prefix'] != 'xxxxxx'):
        sys.stdout.write("yes")
    else:
        sys.stdout.write("no")


if __name__ == "__main__":
    main()
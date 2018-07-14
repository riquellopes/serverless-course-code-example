import os


def hello(event, context):
    return os.environ.get("FIST_NAME")

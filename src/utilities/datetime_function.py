from datetime import datetime


def create_timestamps():
    return datetime.now().replace(microsecond=0).timestamp()

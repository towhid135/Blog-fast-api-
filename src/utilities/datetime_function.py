from datetime import datetime,timezone


def create_timestamps():
    timestamp_utc = datetime.now(tz=timezone.utc).replace(microsecond=0).timestamp()
    return timestamp_utc

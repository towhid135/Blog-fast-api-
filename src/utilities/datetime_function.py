from datetime import datetime, timezone, timedelta


def create_timestamps():
    timestamp_utc = datetime.now(tz=timezone.utc).replace(microsecond=0).timestamp()
    return timestamp_utc


def adjust_current_time_in_utc(operation, minutes):
    """
    This function adjust the current time based on the operation.
    Args:
        operation: A string indicating the operation to perform (add, sub).
        minutes: The number of minutes to add or subtract (integer).
    Returns:
        Returns a timestamp in utc format.
    """
    if operation not in ("add", "sub"):
        raise ValueError("Invalid operation. Please use add or sub")
    delta = timedelta(minutes=minutes)
    now = datetime.now(tz=timezone.utc)
    if operation == "add":
        timestamp_utc = (now + delta).replace(microsecond=0).timestamp()
        return timestamp_utc
    else:
        timestamp_utc = (now - delta).replace(microsecond=0).timestamp()
        return timestamp_utc

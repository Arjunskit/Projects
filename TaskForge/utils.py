from datetime import datetime

VALID_PRIORITIES = ["Low", "Medium", "High"]
VALID_STATUSES = ["Pending", "Completed"]


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def validate_priority(priority):
    return priority.capitalize() in VALID_PRIORITIES


def validate_status(status):
    return status.capitalize() in VALID_STATUSES

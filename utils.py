"""Utilities for app.py"""
import datetime
from bson.objectid import ObjectId

def created_today(entry_id):
    """Checks if the given record was created today, so a New badge can be displayed for it"""
    obj_id = ObjectId(entry_id)
    create_date = obj_id.generation_time.date()
    today = datetime.datetime.utcnow().date()
    return (create_date == today)

from datetime import datetime
from typing import Dict

TOGGL_ENTRY_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"  # 2018-01-29T08:10:49+00:00


class TogglEntry:
    def __init__(self, entry_dict: Dict[str, object]):
        if "description" in entry_dict:
            self.title = entry_dict["description"]
        else:
            self.title = None
        if "tags" in entry_dict:
            self.tags = entry_dict["tags"]
        else:
            self.tags = None
        self.start_datetime = datetime.strptime(entry_dict["start"], TOGGL_ENTRY_TIME_FORMAT)
        if "stop" in entry_dict:
            self.stop_datetime = datetime.strptime(entry_dict["stop"], TOGGL_ENTRY_TIME_FORMAT)
        else:
            self.stop_datetime = datetime.now()
        self.duration = entry_dict["duration"]

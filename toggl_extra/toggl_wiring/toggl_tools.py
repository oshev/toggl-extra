import json
from datetime import datetime

import requests

TOGGL_URL_TEMPLATE = "https://www.toggl.com/api/v8/time_entries?start_date={}&end_date={}"
TOGGL_TIME_FORMAT = "%Y-%m-%dT%H:%M:00Z"


def get_entries(api_token: str, start_datetime: datetime, end_datetime: datetime = datetime.now()):
    """
    Retrieve Toggl time entries for a given date-time interval.

    :param api_token: API token to access user's Toggl data.
    :param start_datetime: Date-time of the interval start.
    :param end_datetime: Date-time of the interval end (by default it is now).
    :return: Toggl time entries as is in JSON format.
    """

    start_date_str = start_datetime.strftime(TOGGL_TIME_FORMAT)
    end_date_str = end_datetime.strftime(TOGGL_TIME_FORMAT)

    response = requests.get(TOGGL_URL_TEMPLATE.format(start_date_str, end_date_str),
                            auth=(api_token, 'api_token'))

    if response.status_code == 200:
        time_entries = json.loads(response.text)
        print("Got {} time entries".format(len(time_entries)))
        return time_entries
    else:
        print("Get error code from the API: {}".format(response.status_code))
        return None

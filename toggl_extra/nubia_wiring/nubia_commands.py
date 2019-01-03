import os
import sys

from nubia import command, argument, context

from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from toggl_extra.toggl_wiring.toggl_tools import get_entries
from toggl_extra.periods import period_times, from_period_type_name

DATE_FORMAT = "%d.%m.%y"


@command("dump_entries")
def dump_entries(period_type_name: str, period_num: int,
                 year: int = datetime.now().year,
                 filename_prefix: str = '/tmp/entries') -> None:
    """
    Dump Toggl entries for a given period to a JSON file.

    :param period_type_name: Name of the period type. Supported now: year, quarter, month, week, or day.
    :param period_num: Order number of the period (e.g. 2nd week of the year, 3rd month).
    :param year: Year of the period (current year by default).
    :param filename_prefix: Prefix of the file where to save the entries. It'll be complemented by the dates and .json.
    :return:
    """
    ctx = context.get_context()
    period_type = from_period_type_name(period_type_name)
    start_datetime, end_datetime = period_times(period_type, period_num, year)

    start_datetime_str = start_datetime.strftime(DATE_FORMAT)
    end_datetime_str = end_datetime.strftime(DATE_FORMAT)

    print(f'Retrieving entries from {start_datetime_str} to {end_datetime_str}...')
    entries = get_entries(ctx.toggl_auth_token, start_datetime, end_datetime)

    if entries:
        output_filename = f'{filename_prefix}_{start_datetime_str}_{end_datetime_str}.json'

        with open(output_filename, 'w') as output:
            output.write(str(entries))
        print(f'Successfully saved to {output_filename}.')


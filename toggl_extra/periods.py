from enum import Enum
from datetime import datetime, timedelta, date
import calendar


class PeriodType(Enum):
    YEAR = 'year'
    QUARTER = 'quarter'
    MONTH = 'month'
    WEEK = 'week'
    DAY = 'day'


def from_period_type_name(period_type_name: str) -> PeriodType:
    """
    Safely get Period Type from its name.

    :param period_type_name: Name of the period type.
    :return: Period type enum.
    """
    period_type_values = [item.value for item in PeriodType]
    if period_type_name.lower() not in period_type_values:
        raise AttributeError(f"Non-existent period type {period_type_name}, supported types: {period_type_values}")
    else:
        return PeriodType(period_type_name.lower())


def period_times(period_type: PeriodType, period_num: int,
                 year: int = datetime.now().year) -> (datetime, datetime):
    """
    Calculate date-time values for the beginning and end of a period defined by type and order number.

    :param period_type: Type of the period: year, quarter, month, week, or day.
    :param period_num: Order number of the period (e.g. 2nd week of the year, 3rd month).
    :param year: Year of the period (current year by default).
    :return: date-time values for the beginning and end of a period defined by type and order number.
    """
    period_number = period_num
    year = year
    period_start, period_end = None, None
    if period_type == PeriodType.YEAR:
        period_start, period_end = _get_year_start_end(year)
    elif period_type == PeriodType.QUARTER:
        _abort_if_period_invalid(period_num, 1, 4, "quarter")
        period_start, period_end = _get_quarter_start_end(year, period_number)
    elif period_type == PeriodType.MONTH:
        _abort_if_period_invalid(period_num, 1, 12, "month")
        # month_name = date(year, period_number, 1).strftime('%B')
        period_start, period_end = _get_month_start_end(year, period_number)
    elif period_type == PeriodType.WEEK:
        _abort_if_period_invalid(period_num, 1, 52, "week")
        period_start, period_end = _get_week_start_end(year, period_number)
    elif period_type == PeriodType.DAY:
        pass  # TODO

    return period_start, period_end


def _abort_if_period_invalid(period_number: int, min_value: int, max_value: int, period_name: str):
    if max_value > period_number < min_value:
        print(f"Wrong {period_name} number, accepted values {min_value}-{max_value}.")
        exit(1)


def _get_year_start_end(year: int) -> (datetime, datetime):
    datetime_start = datetime.combine(date(year, 1, 1), datetime.min.time())
    datetime_end = datetime.combine(date(year, 12, 31), datetime.max.time())
    return datetime_start, datetime_end


def _get_quarter_start_end(year: int, quarter: int) -> (datetime, datetime):
    first_month_of_quarter = 3 * quarter - 2
    last_month_of_quarter = 3 * quarter
    date_of_first_day_of_quarter = date(year, first_month_of_quarter, 1)
    date_of_last_day_of_quarter = date(year, last_month_of_quarter,
                                       calendar.monthrange(year, last_month_of_quarter)[1])
    datetime_start = datetime.combine(date_of_first_day_of_quarter, datetime.min.time())
    datetime_end = datetime.combine(date_of_last_day_of_quarter, datetime.max.time())
    return datetime_start, datetime_end


def _get_month_start_end(year: int, month: int) -> (datetime, datetime):
    month_end_date = calendar.monthrange(year, month)[1]
    datetime_start = datetime.combine(date(year, month, 1), datetime.min.time())
    datetime_end = datetime.combine(date(year, month, month_end_date), datetime.max.time())
    return datetime_start, datetime_end


def _get_week_start_end(year: int, week: int) -> (datetime, datetime):
    first_date = date(int(year), 1, 1)
    date_end = date(int(year) + 1, 1, 7)
    while first_date < date_end:
        if first_date.isocalendar()[1] == week + 1 and first_date.isocalendar()[0] == year:
            break
        first_date += timedelta(days=1)
    datetime_start = datetime.combine(first_date, datetime.min.time()) - timedelta(days=7)
    datetime_end = datetime.combine(datetime_start.date() + timedelta(days=6), datetime.max.time())
    return datetime_start, datetime_end

from datetime import datetime, timedelta
from lib.util import extract

DEFAULT_DATE_FORMAT = "%Y-%m-%d"

def calculate(offset=0):
    return datetime.today() + timedelta(days=offset)

def parse(date_str, date_format = DEFAULT_DATE_FORMAT):
    if date_str == 'yesterday':
        return calculate(-1)
    elif date_str == 'today':
        return calculate(0)
    else:
        return datetime.strptime(date_str, date_format)

def format(date, date_format = DEFAULT_DATE_FORMAT):
    return datetime.strftime(date, date_format)

def today():
    return datetime.today()

def yesterday():
    return calculate(-1)

def date_range(from_date, to_date):
    n_days = (to_date - from_date).days
    return [from_date + timedelta(days=x) for x in range(0, n_days+1)]

def parse_range(date_range_str):
    dates = extract('^(\d+-\d+-\d+)-(\d+-\d+-\d+)$', date_range_str)
    return date_range(parse(dates[0]), parse(dates[1])) if dates else None

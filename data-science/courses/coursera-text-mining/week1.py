import pandas as pd
import os
import re
import datetime

DATA_PATH = os.path.expanduser('~/Dropbox/data/projects/courses/coursera-text-mining/course4_downloads/dates.txt')
lines = [l.strip() for l in open(DATA_PATH)]

def parse_date(line):
  # TODO: refactor to used named capture groups with (?P<group_name>)
  # NOTE: it's mm/dd/yy or mm/yy
  day_pattern = r'([1-9]|0[1-9]|1[012])(?:/|-)(\d{1,2})(?:/|-)(19\d\d|20\d\d|\d\d)'
  month_pattern = r'([1-9]|0[1-9]|1[012])/(19\d\d|20\d\d|\d\d)'
  month_prefixes = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  month_prefixes_pattern = '|'.join([p + r'\w*' for p in month_prefixes])
  # 25 June, 2012
  month_name_middle_pattern = rf'(?:(\d{{1,2}})[,.\s]+)?({month_prefixes_pattern})[,.\s]+(\d\d\d\d)'
  # June 25, 2012
  month_name_prefix_pattern = rf'({month_prefixes_pattern})[,.\s]+(\d{{1,2}})[,.\s]+(\d\d\d\d)'
  year_pattern = r'(19\d\d|20\d\d)'
  def first_match(patterns):
    for i, p in enumerate(patterns):
      m = re.search(p, line)
      if m:
        #print(f'matching pattern i={i}')
        return [p for p in m.groups() if p]
  parts = first_match([day_pattern, month_pattern, month_name_middle_pattern, month_name_prefix_pattern, year_pattern])
  def parse_month(month):
    prefixes = [p for p in month_prefixes if str(month).startswith(p)]
    if prefixes:
      return month_prefixes.index(prefixes[0]) + 1
    else:
      return int(month)
  def parse_year(year):
    if len(year) == 2:
      return 1900 + int(year)
    elif int(year) > 1900 and int(year) < 2020:
      return int(year)
    else:
      raise ValueError(f'Invalid year={year}')
  if parts:
    if len(parts) == 1:
      day = 1
      month = 1
      year = parts[0]
    elif len(parts) == 2:
      day = 1
      month, year = parts
    else:
      if re.match(r'^\d+$', parts[1]):
        month, day, year = parts
      else:
        day, month, year = parts
    try:
      result = datetime.date(parse_year(year), parse_month(month), int(day))
      #print(f'line={line}')
      #print(f'result={result} parts={parts} len={len(parts)} year={year} month={month} day={day}\n')
      return result
    except:
      return None

dates = [parse_date(l) for l in lines]
dates_parsed = [d for d in dates if d]
print(f'Number of parsed dates: {len(dates_parsed)}/{len(lines)}')

for date, line in zip(dates, lines):
  print(f'date={date} line={line}')

sorted_lines = sorted(lines, key=parse_date)
result = [lines.index(l) for l in sorted_lines]

def from_iso_date(date_str):
  return datetime.datetime.strptime(date_str, '%Y-%m-%d')

def to_iso_date(date):
  return datetime.datetime.strftime(date, '%Y-%m-%d')

test_cases = [
  ['03/25/93 Total time of visit (in minutes):', '1993-03-25'],
  ['6/18/85 Primary Care Doctor:', '1985-06-18'],
  ['9/1980 Primary Care Doctor:', '1980-09-01'],
  ['sshe plans to move as of 7/8/71 In-Home Services: None', '1971-07-08'],
  ['1/25/2011 CPT Code: 90792: With medical services', '2011-01-25'],
  ['30 Nov 2007 CPT Code: 90801 - Psychiatric Diagnosis Interview', '2007-11-30'],
  ['September 01, 2012 Age:', '2012-09-01'],
  ['July 25, 1983 Total time of visit (in minutes):', '1983-07-25'],
  ['August 11, 1989 Total time of visit (in minutes):', '1989-08-11'],
  ['2008 partial thyroidectomy', '2008-01-01']
]

failures = []
for line, expected in test_cases:
  actual = to_iso_date(parse_date(line))
  if expected != actual:
    failures.append({'line': line, 'expected': expected, 'actual': actual})
print(f'Number of failures: {len(failures)}')
print(failures)

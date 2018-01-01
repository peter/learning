def maskify1(cc):
  MASK_CHAR = '#'
  START_LENGTH = 1
  END_LENGTH = 4
  MIN_LENGTH = START_LENGTH + END_LENGTH + 1
  if len(cc) < MIN_LENGTH:
    return cc
  mask_range = range(START_LENGTH, (len(cc) - END_LENGTH))
  def should_mask(i, c):
    return c.isdigit() and i in mask_range
  result = ''
  for i, c in enumerate(cc):
    result += MASK_CHAR if should_mask(i, c) else c
  return result

def maskify2(cc):
  MASK_CHAR = '#'
  if len(cc) < 6:
    return cc
  mask_range = range(1, (len(cc) - 4))
  def should_mask(i, c):
    return c.isdigit() and i in mask_range
  def get_char(i, c):
    return MASK_CHAR if should_mask(i, c) else c
  chars = [get_char(i, c) for (i, c) in enumerate(cc)]
  return ''.join(chars)

def numbertoordinal(number):
  assert(isinstance(number, int) and number >= 0)
  if number == 0:
    return str(number)
  last_digit = number % 10
  default_suffix = 'th'
  suffixes = {
    1: 'st',
    2: 'nd',
    3: 'rd'
  }
  suffix = suffixes.get(last_digit, default_suffix)
  return str(number) + suffix

import re
def calculate(expression):
  if expression is None or len(expression) == 0:
    return 0
  assert(isinstance(expression, str) and
         re.match('^([0-9+*/ .-])*$', expression))
  numbers = []
  operators = {
    '+': lambda l, r: l + r,
    '-': lambda l, r: l - r,
    '*': lambda l, r: l * r,
    '/': lambda l, r: l / r
  }
  def parse_number(item):
    try:
      return int(item) if item.isdigit() else float(item)
    except ValueError:
      return None
  for pos, item in enumerate(expression.split(' ')):
    number = parse_number(item)
    if number:
      numbers.append(number)
    elif item in operators:
      if len(numbers) < 2:
        raise ValueError('Missing operands for %s at position %s' % (item, pos))
      right_operand = numbers.pop()
      left_operand = numbers.pop()
      result = operators[item](left_operand, right_operand)
      numbers.append(result)
    else:
      raise ValueError('Could not parse %s at position %s' % (item, pos))
  if len(numbers) == 0:
    raise ValueError('No numbers at end of calculation')
  return numbers[-1]

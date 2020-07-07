import pgzrun
import math
from types import SimpleNamespace
import time

WIDTH = 600
HEIGHT = 600

start_x = WIDTH/2
start_y = HEIGHT/2
start_pos = (start_x, start_y)
radius = 80
speed = 5
center_pos = (start_x, start_y + radius)
draw_radius = 5

def draw():
  screen.fill('blue')
  screen.draw.circle(center_pos, radius, 'red')
  screen.draw.filled_circle(center_pos, draw_radius, 'red')

  screen.draw.filled_circle(start_pos, draw_radius, 'yellow')

  # Upper right quadrant
  angle = math.pi / 4
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  screen.draw.filled_circle((x, y), draw_radius, 'yellow')

  # Lower right quadrant
  angle = math.pi * 3 / 4
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  screen.draw.filled_circle((x, y), draw_radius, 'yellow')

  # Lower left quadrant
  angle = math.pi * 5 / 4
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  screen.draw.filled_circle((x, y), draw_radius, 'yellow')

  # Uppre left quadrant
  angle = math.pi * 7 / 4
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  screen.draw.filled_circle((x, y), draw_radius, 'yellow')

pgzrun.go() # Must be last line

import pgzrun
import math
from types import SimpleNamespace
import time

WIDTH = 600
HEIGHT = 600

start_x = WIDTH/2
start_y = HEIGHT/2
angle = 0
x = start_x
y = start_y
start_pos = (start_x, start_y)
radius = 80
speed = 15
center_pos = (start_x, start_y + radius)
draw_radius = 5

def update_angle(speed, radius, angle):
  return (angle + speed/radius) % (2 * math.pi)

def pos_from_angle(start_pos, radius, angle):
  center_pos = (start_pos[0], start_pos[1] + radius)
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  return (x, y)

def update():
  global angle
  angle = update_angle(speed, radius, angle)

def draw():
  screen.fill('blue')
  screen.draw.circle(center_pos, radius, 'red')
  screen.draw.filled_circle(center_pos, draw_radius, 'red')
  screen.draw.filled_circle(pos_from_angle(start_pos, radius, angle), draw_radius, 'yellow')

pgzrun.go() # Must be last line

import pgzrun
import math
from types import SimpleNamespace

WIDTH = 600
HEIGHT = 600

start_x = WIDTH/2
start_y = HEIGHT/2
start_pos = (start_x, start_y)
bird = SimpleNamespace(**{
  'angle': 0,
  'angle_update': 0.06,
  'speed': 5,
  'last_dx': None,
  'last_dy': None,
  'max': {'x': start_x, 'y': start_y},
  'min': {'x': start_x, 'y': start_y},
  'actor': Actor('bird0', start_pos)
})
print(f'angle={bird.angle} speed={bird.speed} start_pos={start_pos}')

def sign(value):
  return 1 if value >= 0 else -1

def update():
  dx = math.cos(bird.angle) * bird.speed
  if bird.last_dx and sign(bird.last_dx) != sign(dx):
    print(f'dx inflection at x={bird.actor.x} y={bird.actor.y}')
    print(f"x max={bird.max['x']} min={bird.min['x']} diameter={bird.max['x'] - bird.min['x']}")
  dy = math.sin(bird.angle) * bird.speed
  if bird.last_dy and sign(bird.last_dy) != sign(dy):
    print(f'dy inflection at x={bird.actor.x} y={bird.actor.y}')
    print(f"y max={bird.max['y']} min={bird.min['y']} diameter={bird.max['y'] - bird.min['y']}")
  bird.actor.x += dx
  bird.actor.y += dy
  bird.last_dx = dx
  bird.last_dy = dy
  bird.max['x'] = max(bird.max['x'], bird.actor.x)
  bird.min['x'] = min(bird.min['x'], bird.actor.x)
  bird.max['y'] = max(bird.max['y'], bird.actor.y)
  bird.min['y'] = min(bird.min['y'], bird.actor.y)
  bird.angle += bird.angle_update

def draw():
  screen.fill('blue')
  bird.actor.draw()

pgzrun.go() # Must be last line

import pgzrun
import math
from types import SimpleNamespace
import time

WIDTH = 600
HEIGHT = 600

laps = 0
frames = 0
start_time = time.time()

start_x = WIDTH/2
start_y = HEIGHT/2
start_pos = (start_x, start_y)
bird = SimpleNamespace(**{
  'angle': 0,
  'radius': 120,
  'speed': 5,
  'last_dx': None,
  'last_dy': None,
  'max': {'x': start_x, 'y': start_y},
  'min': {'x': start_x, 'y': start_y},
  'actor': Actor('bird0', start_pos)
})

print(f'radius={bird.radius} speed={bird.speed}')

def sign(value):
  return 1 if value >= 0 else -1

def update_angle(speed, radius, angle):
  return (angle + speed/radius) % (2 * math.pi)

def pos_from_angle(start_pos, radius, angle):
  center_pos = (start_pos[0], start_pos[1] + radius)
  x = center_pos[0] + math.sin(angle) * radius
  y = center_pos[1] - math.cos(angle) * radius
  return (x, y)

def update():
  global frames, laps
  frames += 1
  bird.angle = update_angle(bird.speed, bird.radius, bird.angle)
  new_pos = pos_from_angle(start_pos, bird.radius, bird.angle)
  dx = new_pos[0] - bird.actor.x
  if bird.last_dx and sign(bird.last_dx) != sign(dx):
    x_radius = (bird.max['x'] - bird.min['x'])/2
    # print(f'dx inflection at x={bird.actor.x} y={bird.actor.y} angle={bird.angle}')
    # print(f"x max={bird.max['x']} min={bird.min['x']} radius={x_radius}")
  dy = new_pos[1] - bird.actor.y
  if bird.last_dy and sign(bird.last_dy) != sign(dy):
    y_radius = (bird.max['y'] - bird.min['y'])/2
    # print(f'dy inflection at x={bird.actor.x} y={bird.actor.y} angle={bird.angle}')
    # print(f"y max={bird.max['y']} min={bird.min['y']} radius={y_radius}")
    if dy > 0:
      laps += 1
      seconds = time.time() - start_time
      circular_distance = 2*math.pi*y_radius*laps
      print(f'laps={laps} frames={frames} seconds={round(seconds, 1)} frames/seconds={round(frames/seconds, 1)} frames/lap={round(frames/laps, 1)}')
      print(f'circular_distance={round(circular_distance, 1)} circular_distance/frame(speed)={round(circular_distance/frames, 1)}')
  bird.actor.x = bird.actor.x + dx
  bird.actor.y = bird.actor.y + dy
  bird.last_dx = dx
  bird.last_dy = dy
  bird.max['x'] = max(bird.max['x'], bird.actor.x)
  bird.min['x'] = min(bird.min['x'], bird.actor.x)
  bird.max['y'] = max(bird.max['y'], bird.actor.y)
  bird.min['y'] = min(bird.min['y'], bird.actor.y)

def draw():
  screen.fill('blue')
  screen.draw.circle((start_pos[0], start_pos[1] + bird.radius), bird.radius, 'red')
  bird.actor.draw()

pgzrun.go() # Must be last line

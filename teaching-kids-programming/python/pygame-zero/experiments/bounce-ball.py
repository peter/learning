import pgzrun
from random import randint

TITLE = 'Bounce Ball'
WIDTH = 800
HEIGHT = 600

gravity = 1

ball = {
  'x': WIDTH / 2,
  'y': HEIGHT / 2,
  'dx': randint(10, 30),
  'dy': -1 * randint(10, 30),
  'radius': randint(10, 20),
  'color': 'red',
  'slow': 3
}

print(ball)

def slow(velocity, amount):
  if velocity > 0:
    return max(0, velocity - amount)
  if velocity < 0:
    return min(0, velocity + amount)
  if velocity == 0:
    return 0

def move_ball():
  ball['x'] += ball['dx']
  ball['y'] += ball['dy']
  ball['dy'] += gravity

def bounce_ball():
  if ball['x'] + ball['radius'] >= WIDTH: # bounce right wall
    ball['x'] = WIDTH - ball['radius']
    ball['dx'] = -1 * slow(ball['dx'], ball['slow'])
  if ball['x'] - ball['radius'] <= 0: # bounce left wall
    ball['x'] = ball['radius']
    ball['dx'] = -1 * slow(ball['dx'], ball['slow'])
  if ball['y'] - ball['radius'] <= 0: # bounce top wall
    ball['y'] = ball['radius']
    ball['dy'] = -1 * slow(ball['dy'], ball['slow'])
  if ball['y'] + ball['radius'] >= HEIGHT: # bounce bottom wall
    ball['y'] = HEIGHT - ball['radius']
    ball['dy'] = -1 * slow(ball['dy'], ball['slow'])

def update():
  move_ball()
  bounce_ball()

def draw():
  screen.fill('blue')
  screen.draw.filled_circle((ball['x'], ball['y']), ball['radius'], ball['color'])

pgzrun.go() # Must be last line
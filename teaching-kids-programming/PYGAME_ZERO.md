# Pygame Zero

## Anatomy of a Game

```python
import pgzrun

TITLE = 'Anatomy of a Game'
WIDTH = 800
HEIGHT = 600

# Invoked 60 times a second by Pygame Zero
def update():
  # Update variables etc.

# Invoked 60 times a second by Pygame Zero after update is invoked
def draw():
  # TODO: draw actors, background, shapes etc.

pgzrun.go() # Must be last line
```

## Text

Outputting some [text](https://pygame-zero.readthedocs.io/en/stable/ptext.html) on the screen:

```python
import pgzrun
import time

TITLE = 'Outputting Text'
WIDTH = 800
HEIGHT = 600

counts = {'update': 0, 'draw': 0}

start_time = time.time()

def update():
  counts['update'] += 1

def draw():
  screen.clear()
  counts['draw'] += 1
  screen.draw.text(f"Update count: {counts['update']}", (10,10), color=(255,255,255), fontsize=30)
  screen.draw.text(f"Draw count: {counts['draw']}", (10,50), color=(255,255,255), fontsize=30)
  elapsed = round(time.time() - start_time)
  screen.draw.text(f"Elapsed seconds: {elapsed}", (10,90), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
```

You can also have some fun with moving the text around of course, like this:

```python
def draw():
  screen.clear()
  counts['draw'] += 1
  screen.draw.text(f"Update count: {counts['update']}", (10,10), color=(255,255,255), fontsize=30)
  screen.draw.text(f"Draw count: {counts['draw']}", ((10 + 2 * counts['draw']) % WIDTH,50), color=(255,255,255), fontsize=30, angle=counts['draw'])
  elapsed = round(time.time() - start_time)
  screen.draw.text(f"Elapsed seconds: {elapsed}", (10 + elapsed * 10,90), color=(255,255,255), fontsize=30)
```

## Bouncing Ball

```python
import pgzrun
from random import randint

TITLE = 'Bounce Ball'
WIDTH = 800
HEIGHT = 600

gravity = 1
control = 1

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

def control_ball():
  if keyboard.up:
    ball['dy'] -= control
  if keyboard.down:
    ball['dy'] += control
  if keyboard.left:
    ball['dx'] -= control
  if keyboard.right:
    ball['dx'] += control

def update():
  move_ball()
  bounce_ball()
  control_ball()

def draw():
  screen.fill('blue')
  screen.draw.filled_circle((ball['x'], ball['y']), ball['radius'], ball['color'])

pgzrun.go() # Must be last line
```
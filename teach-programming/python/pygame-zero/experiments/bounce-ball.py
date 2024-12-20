from math import sqrt
import pgzrun
from random import randint

# TODO: don't update score if last score was at the same position
# TODO: randomize number of obstacles
# TODO: make obstacles have different speed
# TODO: make obstacles have x movement
# TODO: init_obstacles when all(obstacle['y'] >= HEIGHT for obstacle in obstacles)
# TODO: oscillate radius of obstacles
# TODO: sound effect on score
# TODO: sound effect on game over
# TODO: allow bounce against obstacle three times before game over?

TITLE = 'Bounce Ball'
WIDTH = 800
HEIGHT = 600

def make_ball():
  return {
    'x': WIDTH / 2,
    'y': HEIGHT / 2,
    'dx': 0,
    'dy': 0,
    'radius': randint(10, 20),
    'color': 'red',
    'slow': 3
  }

def make_obstacle():
  radius = randint(10, 30)
  return {
    'x': randint(0 + radius, WIDTH - radius),
    'y': 0,
    'radius': radius,
    'color': 'yellow'
  }

def init_obstacles():
  global obstacles
  obstacles = [make_obstacle() for _ in range(0, 2)]

def init_game():
  global ball, obstacles, score, game_over, gravity, control
  ball = make_ball()
  init_obstacles()
  game_over = False
  score = 0
  gravity = 1
  control = 1

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

def update_score():
  global score
  def ball_above_obstacle(obstacle):
    in_x_interval = ball['x'] >= (obstacle['x'] - abs(ball['dx'])) and ball['x'] <= (obstacle['x'] + abs(ball['dx']))
    return in_x_interval and (ball['y'] + ball['radius']) < obstacle['y']
  for obstacle in obstacles:
    if ball_above_obstacle(obstacle) and not obstacle.get('scored'):
      score += 1
      obstacle['scored'] = True

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

def scroll_obstacles():
  global obstacles
  for obstacle in obstacles:
    obstacle['y'] += 2
  def is_overflow(obstacle):
    return obstacle['y'] >= (HEIGHT - obstacle['radius'])
  def make_if_overflow(obstacle):
    return make_obstacle() if is_overflow(obstacle) else obstacle
  obstacles = [make_if_overflow(obstacle) for obstacle in obstacles]

def draw_ball(ball):
  screen.draw.filled_circle((ball['x'], ball['y']), ball['radius'], ball['color'])

def ball_distance(ball1, ball2):
  return sqrt(abs(ball1['x'] - ball2['x']) ** 2 + abs(ball1['y'] - ball2['y']) ** 2)

def ball_collision(ball1, ball2):
  return ball_distance(ball1, ball2) <= (ball1['radius'] + ball2['radius'])

def update():
  global game_over
  if keyboard.space:
    init_game()
  if game_over:
    return
  move_ball()
  bounce_ball()
  control_ball()
  scroll_obstacles()
  game_over = any(ball_collision(ball, obstacle) for obstacle in obstacles)
  update_score()

def draw():
  if game_over:
    screen.draw.text(f"Game Over", (WIDTH/2,HEIGHT/2), color=(255,255,255), fontsize=30)
    return
  screen.fill('blue')
  screen.draw.text(str(score), (5, 5), color=(255,255,255), fontsize=30)
  draw_ball(ball)
  for obstacle in obstacles:
    draw_ball(obstacle)

init_game()

pgzrun.go() # Must be last line

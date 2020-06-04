import pgzrun
import math

WIDTH = 600
HEIGHT = 600

config = {
  'wave_length': 120,
  'amplitude': 100
}

wave_length = config['wave_length']
angle = 0
frames = 0
start_pos = (WIDTH/2, HEIGHT/2)
positions = [start_pos]

def sine_angle(x_delta):
  return 2 * math.pi * x_delta/wave_length

def sine_y(x_delta, wave_length):
  return math.sin(sine_angle(x_delta)) * config['amplitude']

def update():
  global frames, angle, positions, wave_length
  frames += 1
  pos = positions[-1]
  x = (pos[0] + 2) % WIDTH
  # if (pos[0] < start_pos[0] and x >= start_pos[0]):
  #   wave_length = wave_length * 2
  #   print(f'wave_length={wave_length}')
  x_delta = x - start_pos[0]
  angle = sine_angle(x_delta)
  y = start_pos[1] + sine_y(x_delta, wave_length) + 0.5 * sine_y(x_delta, wave_length*2)
  positions.append((x, y))

def draw_sine_circles():
  for pos in positions:
    screen.draw.filled_circle(pos, 3, 'red')

def draw_sine_clock():
  x = start_pos[0] + math.sin(angle) * config['amplitude']
  y = start_pos[1] - math.cos(angle) * config['amplitude']
  screen.draw.line(start_pos, (x, y), 'yellow')

def draw():
  screen.fill('blue')
  draw_sine_circles()
  draw_sine_clock()

pgzrun.go() # Must be last line

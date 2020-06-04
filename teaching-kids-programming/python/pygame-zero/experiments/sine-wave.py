import pgzrun
import math

WIDTH = 600
HEIGHT = 600

config = {
  'wave_length': 120,
  'amplitude': 100
}

wave_length = config['wave_length']
frames = 0
start_pos = (WIDTH/2, HEIGHT/2)
positions = [start_pos]

def sine_y(x_delta, wave_length):
  return math.sin(2 * math.pi * x_delta/wave_length) * config['amplitude']

def update():
  global frames, positions, wave_length
  frames += 1
  pos = positions[-1]
  x = (pos[0] + 3) % WIDTH
  # if (pos[0] < start_pos[0] and x >= start_pos[0]):
  #   wave_length = wave_length * 2
  #   print(f'wave_length={wave_length}')
  x_delta = x - start_pos[0]
  y = start_pos[1] + sine_y(x_delta, wave_length) + 0.5 * sine_y(x_delta, wave_length*2)
  positions.append((x, y))

def draw():
  screen.fill('blue')
  for pos in positions:
    screen.draw.filled_circle(pos, 3, 'red')

pgzrun.go() # Must be last line

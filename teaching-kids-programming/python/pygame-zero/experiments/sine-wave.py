import pgzrun
import math

WIDTH = 600
HEIGHT = 600

config = {
  'wave_length': 120,
  'amplitude': 100
}

frames = 0
start_pos = (WIDTH/2, HEIGHT/2)
positions = [start_pos]

def update():
  global frames, positions
  frames += 1
  pos = positions[-1]
  x = (pos[0] + 3) % WIDTH
  y = start_pos[1] + math.sin(2 * math.pi * (x - start_pos[0])/config['wave_length']) * config['amplitude']
  positions.append((x, y))

def draw():
  screen.fill('blue')
  for pos in positions:
    screen.draw.filled_circle(pos, 3, 'red')

pgzrun.go() # Must be last line

import pgzrun
import math

WIDTH = 600
HEIGHT = 600

config = {
  'wave_length': 80,
  'amplitude': 30
}

frames = 0
start_pos = (WIDTH/2, HEIGHT/2)
pos = start_pos

def update():
  global frames, pos
  frames += 1
  x = (pos[0] + 3) % WIDTH
  y = start_pos[1] + math.sin((x - start_pos[0])/600 * 4 * math.pi) * 100
  pos = (x, y)

def draw():
  screen.fill('blue')
  screen.draw.filled_circle(pos, 10, 'red')

pgzrun.go() # Must be last line

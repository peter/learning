import pgzrun
import math

WIDTH = 800
HEIGHT = 600

bird = Actor('bird0', (WIDTH/2, HEIGHT/2))
angle = 0
speed = 10

def update():
  global angle
  bird.x += math.cos(angle) * speed
  bird.y += math.sin(angle) * speed
  angle += 0.1

def draw():
  screen.fill('blue')
  bird.draw()

pgzrun.go() # Must be last line

import pgzrun

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

scroll_speed = -1

barry_the_bird = Actor('bird1', (75, 350))
barry_the_bird.speed = 1

gap = 140
top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))

def draw():
    screen.blit('cascade', (0, 0))
    barry_the_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()

def update():
    barry_the_bird.y += barry_the_bird.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right <= 0:
      top_pipe.left = WIDTH
      bottom_pipe.left = WIDTH

def on_mouse_down():
    barry_the_bird.y -= 50

pgzrun.go() # Must be last line

import pgzrun

TITLE = 'Galaga'
WIDTH = 800
HEIGHT = 600

ship_move = 5

ship = Actor('ship')
ship.x = WIDTH/2
ship.bottom = HEIGHT - 10

def update():
  if keyboard.left:
    ship.x -= ship_move
  elif keyboard.right:
    ship.x += ship_move

def draw():
  screen.clear()
  ship.draw()

pgzrun.go()

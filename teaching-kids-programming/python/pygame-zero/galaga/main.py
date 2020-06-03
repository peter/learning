import pgzrun

TITLE = 'Galaga'
WIDTH = 800
HEIGHT = 600

ship_move = 5
bullet_move = 10

ship = Actor('ship')
ship.x = WIDTH/2
ship.bottom = HEIGHT - 10

bullets = []

def shoot():
  bullets.append(Actor('bullet', (ship.x, ship.y)))

def on_key_down(key):
  if key == keys.SPACE:
    shoot()

def update():
  if keyboard.left:
    ship.x -= ship_move
  elif keyboard.right:
    ship.x += ship_move
  for bullet in bullets:
    bullet.y -= bullet_move
    if bullet.y < 0:
      bullets.remove(bullet)

def draw():
  screen.clear()
  for bullet in bullets:
    bullet.draw()
  ship.draw()

pgzrun.go()

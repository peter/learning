import pgzrun

config = {
  'title': 'Galaga',
  'width': 800,
  'height': 600,
  'n_enemies': 3,
  'ship_move': 5,
  'bullet_move': 10,
  'enemy_move': 3
}

TITLE = config['title']
WIDTH = config['width']
HEIGHT = config['height']

def init_ship():
  global ship, bullets
  ship = Actor('ship')
  ship.x = WIDTH/2
  ship.bottom = HEIGHT - 10
  bullets = []

def init_enemies():
  global enemies
  enemies = []
  for n in range(0, config['n_enemies']):
    imageName = 'enemy1'
    x = WIDTH/2 + n * (getattr(images, imageName).get_width() + 5)
    enemy = Actor(imageName, (x, 0))
    enemies.append(enemy)

def init_game():
  init_ship()
  init_enemies()

def shoot():
  bullets.append(Actor('bullet', (ship.x, ship.y)))

def on_key_down(key):
  if key == keys.SPACE:
    shoot()

def update():
  if keyboard.left:
    ship.x -= config['ship_move']
  elif keyboard.right:
    ship.x += config['ship_move']
  for enemy in enemies:
    enemy.y += config['enemy_move']
  if enemies[0].y > HEIGHT:
    init_enemies()
  for bullet in bullets:
    bullet.y -= config['bullet_move']
    if bullet.y < 0:
      bullets.remove(bullet)

def draw():
  screen.clear()
  for enemy in enemies:
    enemy.draw()
  for bullet in bullets:
    bullet.draw()
  ship.draw()

init_game()

pgzrun.go()

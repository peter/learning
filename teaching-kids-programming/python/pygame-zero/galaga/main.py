import pgzrun
from random import randint

config = {
  'title': 'Galaga',
  'width': 800,
  'height': 600,
  'n_enemies': 5,
  'ship_move': 5,
  'bullet_move': 10,
  'enemy_move': 3,
  'enemy_score': 100
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
  imageName = 'enemy1'
  width = getattr(images, imageName).get_width() + 5
  x_first = randint(0, WIDTH - config['n_enemies'] * width)
  for n in range(0, config['n_enemies']):
    x = x_first + n * width
    enemy = Actor(imageName, (x, 0))
    enemies.append(enemy)

def init_game():
  global score, game_over
  score = 0
  game_over = False
  init_ship()
  init_enemies()

def shoot():
  bullets.append(Actor('bullet', (ship.x, ship.y)))

def on_key_down(key):
  if key == keys.SPACE:
    shoot()

def update():
  global game_over
  if keyboard[keys.RETURN]:
    init_game()
  if game_over:
    return
  global score
  if keyboard.left:
    ship.x -= config['ship_move']
  elif keyboard.right:
    ship.x += config['ship_move']
  for bullet in bullets:
    bullet.y -= config['bullet_move']
    if bullet.y < 0:
      bullets.remove(bullet)
  for enemy in enemies:
    enemy.y += config['enemy_move']
    if ship.colliderect(enemy):
      game_over = True
      return
    for bullet in bullets:
      if enemy.colliderect(bullet):
        score += config['enemy_score']
        enemies.remove(enemy)
        bullets.remove(bullet)
  if not enemies or enemies[0].y > HEIGHT:
    init_enemies()

def draw():
  if game_over:
    screen.draw.text(f"Game Over (press return to restart)", centerx=WIDTH/2, centery=HEIGHT/2, color=(255,255,255), fontsize=30)
    return
  screen.clear()
  screen.draw.text(str(score), (5, 5), color=(255,255,255), fontsize=30)
  for enemy in enemies:
    enemy.draw()
  for bullet in bullets:
    bullet.draw()
  ship.draw()

init_game()

pgzrun.go()

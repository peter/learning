import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

ship = Actor('player/spaceships/playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('items/gemgreen.png')

def init_gem_position():
    gem.x = random.randint(20, 780)
    gem.y = 0

init_gem_position()

def draw():
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Final Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
    else:
        ship.draw()
        gem.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

def update():
    global score, game_over
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        game_over = True
    if gem.colliderect(ship):
        score += 1
        init_gem_position()

pgzrun.go() # Must be last line

# https://github.com/ericclack/pygamezero_pacman/blob/master/pacman2.py
import pgzrun
import random

TITLE = 'pacman'
SPEED = 2
GHOST_SPEED = 1
WORLD_SIZE = 20
BLOCK_SIZE = 32
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = WORLD_SIZE*BLOCK_SIZE

char_to_image = {
  '.': 'dot.png',
  '=': 'wall.png',
  '*': 'power.png',
  'g': 'ghost1.png',
  'G': 'ghost2.png',
}

world = []
ghosts = []

def set_random_dir(sprite, speed):
    sprite.dx = random.choice([-speed, speed])
    sprite.dy = random.choice([-speed, speed])

def make_ghost_actors():
    for y, row in enumerate(world):
        for x, block in enumerate(row):
            if block == 'g' or block == 'G':
                g = Actor(char_to_image[block], (x*BLOCK_SIZE, y*BLOCK_SIZE), anchor=('left', 'top'))
                set_random_dir(g, GHOST_SPEED)
                ghosts.append(g)
                # Now we have the ghost sprite we don't need this block
                world[y][x] = None

def load_level(level):
  filename = f'level-{level}.txt'
  with open(filename) as f:
    for line in f:
      line = line.rstrip("\n")
      if len(line) < WORLD_SIZE:
        line += ' ' * (WORLD_SIZE - len(line))
      row = [block for block in line]
      print(f'row: {row}')
      world.append(row)

def assert_world_size():
  assert len(world) == WORLD_SIZE, f'len(world)={len(word)} but should be {WORLD_SIZE}'
  for i, row in enumerate(world):
    assert len(row) == WORLD_SIZE, f'i={i} len(row)={len(row)} but should be {WORLD_SIZE}'

load_level(1)
assert_world_size()
make_ghost_actors()

pacman = Actor('pacman_o.png', anchor=('left', 'top'))
pacman.x = pacman.y = 1*BLOCK_SIZE
pacman.dx, pacman.dy = 0,0

def blocks_ahead_of(sprite, dx, dy):
  # Here's where we want to move to
  x = sprite.x + dx
  y = sprite.y + dy

  # Find integer block pos, using floor (so 4.7 becomes 4)
  ix,iy = int(x // BLOCK_SIZE), int(y // BLOCK_SIZE)
  # Remainder let's us check adjacent blocks
  rx, ry = x % BLOCK_SIZE, y % BLOCK_SIZE
  if ix == WORLD_SIZE-1: rx = 0
  if iy == WORLD_SIZE-1: ry = 0

  blocks = [ world[iy][ix] ]
  if rx: blocks.append(world[iy][ix+1])
  if ry: blocks.append(world[iy+1][ix])
  if rx and ry: blocks.append(world[iy+1][ix+1])

  # if dx != 0 or dy != 0:
  #   print(f'blocks_ahead (x={pacman.x}, y={pacman.y}) -> (x={x}, y={y})')
  #   print(f'blocks_ahead ix={ix}, iy={iy}, rx={rx}, ry={ry}')
  #   print(f'world[iy][ix]: "{world[iy][ix]}"')
  #   print(f'world[iy][ix+1]: "{world[iy][ix+1]}"')
  #   print(f'world[iy+1][ix]: "{world[iy+1][ix]}"')
  #   print(f'world[iy+1][ix+1]: "{world[iy+1][ix+1]}"')
  #   print(f'blocks={blocks}')

  return blocks

def wrap_around(mini, val, maxi):
    if val < mini: return maxi
    elif val > maxi: return mini
    else: return val

def on_key_down(key):
    if key == keys.LEFT:
        pacman.dx = -1
    if key == keys.RIGHT:
        pacman.dx = 1
    if key == keys.UP:
        pacman.dy = -1
    if key == keys.DOWN:
        pacman.dy = 1

def on_key_up(key):
    if key in (keys.LEFT, keys.RIGHT):
        pacman.dx = 0
    if key in (keys.UP, keys.DOWN):
        pacman.dy = 0

def move_ahead(sprite):
    # Record current pos so we can see if the sprite moved
    oldx, oldy = sprite.x, sprite.y

    # In order to go in direction dx, dy there must be no wall that way
    if '=' not in blocks_ahead_of(sprite, sprite.dx, 0):
        sprite.x += sprite.dx
    if '=' not in blocks_ahead_of(sprite, 0, sprite.dy):
        sprite.y += sprite.dy

    # Keep sprite on the screen
    sprite.x = wrap_around(0, sprite.x, WIDTH-BLOCK_SIZE)
    sprite.y = wrap_around(0, sprite.y, HEIGHT-BLOCK_SIZE)

    # Return whether we moved
    return oldx != sprite.x or oldy != sprite.y

def update():
    move_ahead(pacman)
    for g in ghosts:
        if not move_ahead(g):
            set_random_dir(g, GHOST_SPEED)

def draw():
  screen.clear()
  for y, row in enumerate(world):
      for x, block in enumerate(row):
          image = char_to_image.get(block, None)
          if image:
              screen.blit(char_to_image[block], (x*BLOCK_SIZE, y*BLOCK_SIZE))
  for g in ghosts: g.draw()
  pacman.draw()

pgzrun.go() # Must be last line

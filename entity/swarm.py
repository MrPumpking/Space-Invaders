from pygame import PixelArray
from pygame.color import Color
from util.timer import Timer
from util.resources import load_image
from pygame import Rect
from random import choice
from projectile.laser import Laser

from entity.ufo import UFO
from entity.dove import Dove
from entity.ligher import Ligher
from entity.ninja import Ninja
from entity.paranoid import Paranoid
from entity.saboteur import Saboteur

CODES = {
  (0, 0, 0): UFO,
  (255, 0, 0): Dove,
  (0, 255, 0): Ligher,
  (0, 0, 255): Ninja,
  (255, 255, 0): Paranoid,
  (0, 255, 255): Saboteur
}

class Swarm():
  def __init__(self, scene, map_path):
    self.scene = scene
    self.surface, _ = load_image(map_path, alpha=False)
    self.map = PixelArray(self.surface)
    self.width = self.map.shape[0]
    self.height = self.map.shape[1]
    self.ships = []
    self.ships_layout = [None] * (self.width * self.height)
    self.direction = 1
    self.velocity = 1
    self.timer = Timer()

    sprite_size = 32
    sprite_scale = 3
    self.scaled_size = sprite_size * sprite_scale

    self.offset_left = 0
    self.offset_right = 0

    self.rect = Rect(0, -(self.height - 3) * self.scaled_size, self.width * self.scaled_size, self.height * self.scaled_size)
    self.decode_map()

  def decode_map(self):
    for y in range(self.height):
      for x in range(self.width):
        colour = self.map[x, y]

        for code, ship in CODES.items():
          if colour == self.surface.map_rgb(code):
            self.ships_layout[y * self.width + x] = ship
            continue

  def spawn(self):
    for y in range(self.height):
      for x in range(self.width):
        ship_class = self.ships_layout[y * self.width + x]

        if ship_class != None:
          ship = ship_class(self.scene)
          ship.rect.move_ip(x * ship.scaled_size, y * ship.scaled_size)
          ship.swarm_x, ship.swarm_y = x, y
          self.ships.append(ship)

  def get_ship_at(self, x, y):
    if x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1:
      return None
    return self.ships[y * self.width + x]

  def shift_down(self):
    self.rect.top += 16

  def get_random_ship(self):
    try:
      return choice([ship for ship in self.ships if ship.health > 0])
    except IndexError:
      return None

  def shoot(self):
    ship = self.get_random_ship()
    if ship != None:
      self.scene.enemy_projectiles.add(Laser(ship.rect, 1, ship.weapon_power))

  def is_column_empty(self, x):
    for ship in self.ships:
      if ship.swarm_x == x:
        return False

    return True

  def is_row_empty(self, y):
    for ship in self.ships:
      if ship.swarm_y == y:
        return False

    return True

  def on_ship_destroyed(self, ship):
    self.ships.remove(ship)
    self.shrink_swarm(ship.swarm_x, ship.swarm_y)

    if len(self.ships) == 0:
      self.scene.game.events.broadcast('SWARM_DESTROYED', {})

  def shrink_swarm(self, x, y):
    if x == 0 and self.is_column_empty(x):
      self.offset_left = self.scaled_size

    elif x == self.width - 1 and self.is_column_empty(x):
      self.offset_right = -self.scaled_size

    elif y == self.height - 1 and self.is_row_empty(y):
      self.rect.height -= self.scaled_size

  def move(self):
    if self.direction == 1 and self.rect.right + self.velocity + self.offset_right > self.scene.game.get_width():
      self.direction = -1
      self.shift_down()

    elif self.rect.left - self.velocity + self.offset_left < 0:
      self.direction = 1
      self.shift_down()

    self.move_ships()
    self.rect.left += self.direction * self.velocity

  def move_ships(self):
    for ship in self.ships:
      if ship != None:
        ship.rect.top = self.rect.top + ship.swarm_y * ship.scaled_size
        ship.rect.left = self.rect.left + ship.swarm_x * ship.scaled_size

  def update(self):
    self.move()
    
    if self.timer.has_passed(1000):
      self.shoot()
        

    

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
    self.ships = [None] * (self.width * self.height)
    self.direction = 1
    self.velocity = 1
    self.timer = Timer()

    sprite_size = 32
    sprite_scale = 2
    scaled_size = sprite_size * sprite_scale

    self.rect = Rect(0, -(self.height - 3) * scaled_size, self.width * scaled_size, self.height * scaled_size)
    self.decode_map()

  def decode_map(self):
    for y in range(self.height):
      for x in range(self.width):
        colour = self.map[x, y]

        for code, ship in CODES.items():
          if colour == self.surface.map_rgb(code):
            ship = ship(self.scene)
            ship.rect.move_ip(x * ship.scaled_size, y * ship.scaled_size)
            ship.swarm_x, ship.swarm_y = x, y
            self.ships[y * self.width + x] = ship
            continue

  def get_ship_at(self, x, y):
    if x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1:
      return None
    return self.ships[y * self.width + x]

  def shift_down(self):
    self.rect.top += 16

  def get_random_ship(self):
    return choice([ship for ship in self.ships if ship != None])

  def shoot(self):
    ship = self.get_random_ship()
    self.scene.enemy_projectiles.add(Laser(ship.rect, 1))

  def remove_ship(self, ship):
    self.ships.remove(ship)

  def move(self):
    if self.direction == 1 and self.rect.right + self.velocity > self.scene.game.get_width():
      self.direction = -1
      self.shift_down()

    elif self.rect.left - self.velocity < 0:
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
        

    

import pygame
import resources

class Laser(pygame.sprite.Sprite):
  def __init__(self, position):
    pygame.sprite.Sprite.__init__(self)
    self.scale = 2
    self.sprite, self.rect = resources.load_image("laser.png", self.scale)

    spawn_x = position.left + (position.width / 2) - (self.rect.width // (2 * self.scale))

    self.rect.move_ip(spawn_x, position.top)

  def update(self):
    self.rect.top -= 5
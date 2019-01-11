import pygame
import resources

class Projectile(pygame.sprite.Sprite):
  def __init__(self, sprite_path, direction, speed = 10, scale = 2):
    super().__init__()
    self.scale = scale
    self.speed = speed
    self.direction = direction
    self.sprite, self.rect = resources.load_image(sprite_path, self.scale)

  def update(self):
    self.rect.top += self.direction * self.speed

  def render(self, surface):
    surface.blit(self.sprite, self.rect)
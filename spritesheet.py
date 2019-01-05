import pygame
import resources

class Spritesheet():
  def __init__(self, path, sprite_size, scale = 1):
    self.sprite_size = sprite_size * scale
    self.sheet, self.rect = resources.load_image(path)
    self.sheet = pygame.transform.scale(self.sheet, (self.rect.width * scale, self.rect.height * scale))

  def get_sprite(self, position):
    rect = (position[0] * self.sprite_size, position[1] * self.sprite_size, self.sprite_size, self.sprite_size)
    sprite = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA, 32).convert_alpha()
    sprite.blit(self.sheet, (0, 0), rect)
    return sprite

  def get_sprites(self, positions):
    return [self.get_sprite(position) for position in positions]
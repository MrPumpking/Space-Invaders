import timer
import pygame
import resources

class AnimatedSprite(pygame.sprite.Sprite):
  def __init__(self, image_path, sprite_size, frames, scale = 1, animation_speed = 10, alpha = 255):
    pygame.sprite.Sprite.__init__(self)
    self.sheet, self.sheet_rect = resources.load_image(image_path)
    self.sheet = pygame.transform.scale(self.sheet, (self.sheet_rect.width * scale, self.sheet_rect.height * scale))

    self.scale = scale
    self.sprite_size = sprite_size
    self.scaled_size = sprite_size * scale
    self.rect = pygame.Rect(0, 0, sprite_size * scale, sprite_size * scale)

    self.animation_frame = 0
    self.animation_max = frames - 1
    self.animation_speed = animation_speed
    self.animation_timer = timer.Timer()

  def render(self, surface, coords = None):
    coords = coords if coords != None else self.rect
    surface.blit(self.sheet, coords, (self.scaled_size * self.animation_frame, 0, self.scaled_size, self.scaled_size))

  def update(self):
    if self.animation_timer.has_passed(self.animation_speed):
      self.animation_frame = 0 if self.animation_frame == self.animation_max else self.animation_frame + 1
import timer
import pygame
import spritesheet

class AnimatedSprite(pygame.sprite.Sprite):
  def __init__(self, spritesheet_path, sprite_size, frames, scale = 1, animation_speed = 10):
    pygame.sprite.Sprite.__init__(self)

    self.spritesheet = spritesheet.Spritesheet(spritesheet_path, sprite_size, scale)
    self.frame_positions = [(i, 0) for i in range(frames)]
    self.sprites = self.spritesheet.get_sprites(self.frame_positions)

    self.rect = pygame.Rect(0, 0, sprite_size * scale, sprite_size * scale)

    self.animation_frame = 0
    self.animation_max = len(self.sprites) - 1
    self.animation_speed = animation_speed
    self.animation_timer = timer.Timer()

    self.sprite = self.sprites[0]

  def update(self):
    if self.animation_timer.has_passed(self.animation_speed):
      self.animation_frame = 0 if self.animation_frame == self.animation_max else self.animation_frame + 1
      self.sprite = self.sprites[self.animation_frame]
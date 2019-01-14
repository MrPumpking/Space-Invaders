from pygame import Rect
from pygame.sprite import Sprite
from util.resources import load_image
from util.timer import Timer

class AnimatedSprite(Sprite):
  def __init__(self, image_path, sprite_size, frames = 1, scale = 1, animation_speed = 10, start_frame = 0):
    super().__init__()
    self._sheet, self._sheet_rect = load_image(image_path, scale)

    self.scale = scale
    self.sprite_size = sprite_size
    self.scaled_size = sprite_size * scale
    self.rect = Rect(0, 0, sprite_size * scale, sprite_size * scale)

    self.animation_frame = start_frame
    self.animation_max = frames - 1
    self.animation_speed = animation_speed
    self.animation_timer = Timer()

  def render(self, surface, coords = None):
    coords = coords if coords != None else self.rect
    surface.blit(self._sheet, coords, (self.scaled_size * self.animation_frame, 0, self.scaled_size, self.scaled_size))

  def update(self):
    if self.animation_timer.has_passed(self.animation_speed):
      self.animation_frame = 0 if self.animation_frame == self.animation_max else self.animation_frame + 1
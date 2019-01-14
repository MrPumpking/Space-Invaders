from laser import Laser
from animated_sprite import AnimatedSprite

class Enemy(AnimatedSprite):
  def __init__(self, screen, sprite_path):
    super().__init__(sprite_path, 32, 4, 3)
    self.screen = screen

  def shoot(self):
    laser = Laser(self.rect, 1)
    self.screen.projectiles.add(laser)
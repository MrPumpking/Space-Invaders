from projectile.laser import Laser
from graphics.animated_sprite import AnimatedSprite

class Enemy(AnimatedSprite):
  def __init__(self, screen, sprite_path, health = 3, points = 50, weapon_power = 1):
    super().__init__(sprite_path, 32, 4, 3, animation_speed=50)
    self.screen = screen
    self.health = health
    self.points = points
    self.swarm_x = 0
    self.swarm_y = 0
    self.weapon_power = weapon_power

  def hit(self, damage):
    self.health -= damage
    return self.health <= 0

  def update(self):
    super().update()
    if self.health <= 0:
      self.kill()
      self.screen.game.events.broadcast('ENEMY_KILLED', { 'points': self.points })

  def shoot(self):
    laser = Laser(self.rect, 1)
    self.screen.projectiles.add(laser)
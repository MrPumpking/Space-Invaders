import pygame.math
from projectile.laser import Laser
from pygame.locals import *
from graphics.animated_sprite import AnimatedSprite
from util.timer import Timer

class Player(AnimatedSprite):
  def __init__(self, scene):
    super().__init__("player.png", 32, 4, 3, 100)
    self.scene = scene
    self.game = self.scene.game
    self.game.events.register_listener('PLAYER_HIT', self.on_hit)

    self.thrust = .8
    self.speed_max = 15
    self.speed_decay = .95
    self.movement_clamp = 10
    self.velocity = pygame.math.Vector2(0, 0)
    self.shoot_delay = 500
    self.shoot_timer = Timer()
    self.shoot_cooldown = False
    self.health = 10
    self.weapon_power = 1

  def on_hit(self, event):
    self.health = max(0, self.health - event.damage)
    self.game.events.broadcast('PLAYER_HEALTH_UPDATE', {})

    if self.health <= 0:
      self.game.events.broadcast('PLAYER_DESTROYED', {})

  def update(self):
    super().update()

    self.move()
    self.shoot()

  def move(self):
    if self.game.input.key(K_LEFT):
      self.velocity.x -= self.thrust
    elif self.game.input.key(K_RIGHT):
      self.velocity.x += self.thrust
    else:
      self.velocity.x *= self.speed_decay

    speed = self.velocity.length()

    if speed > self.speed_max:
      self.velocity.x *= self.speed_max / speed
      self.velocity.y *= self.speed_max / speed
    elif (self.velocity.x > -.5 and self.velocity.x < 0) or (self.velocity.x < .5 and self.velocity.x > 0):
      self.velocity.x = 0

    if (
      self.rect.left - self.movement_clamp < 0 and self.velocity.x < 0 or
      self.rect.left > self.game.get_width() - self.rect.width - self.movement_clamp and self.velocity.x > 0
      ):
      self.velocity.x = 0

    self.rect.move_ip(self.velocity.x, self.velocity.y)

  def shoot(self):
    if self.shoot_cooldown and self.shoot_timer.has_passed(self.shoot_delay):
      self.shoot_cooldown = False

    if self.game.input.key(K_SPACE) and not self.shoot_cooldown:
      self.scene.projectiles.add(Laser(self.rect, power=self.weapon_power))
      self.shoot_cooldown = True
      self.shoot_timer.restart()
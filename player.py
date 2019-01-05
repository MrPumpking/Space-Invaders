import pygame.math
from pygame.locals import *
from animated_sprite import AnimatedSprite

class Player(AnimatedSprite):
  def __init__(self, game):
    AnimatedSprite.__init__(self, "Lightning.png", 32, 4, 3, 100)
    self.game = game
    self.width = self.rect.width

    self.velocity = pygame.math.Vector2(0, 0)
    self.acceleration = pygame.math.Vector2(1, 0)
    self.acceleration_initial = pygame.math.Vector2(0, 0)

    self.velocity_increment = 0.05
    self.velocity_decrement = 0.005
    self.acceleration_increment = 0.05
    self.acceleration_decrement = 0.005

    self.movement_clamp = 10

  def update(self):
    AnimatedSprite.update(self)
    self.handle_movement()
    
  def handle_movement(self):
    if self.game.input.is_key_down(K_RIGHT):
      self.velocity.x = min(5, self.velocity.x + self.velocity_increment)
      self.acceleration.x = min(5, self.acceleration.x + self.acceleration_increment)

    elif self.game.input.is_key_down(K_LEFT):
      self.velocity.x = max(-5, self.velocity.x - self.velocity_increment)      
      self.acceleration.x = min(5, self.acceleration.x + self.acceleration_increment)

    else:
      if self.velocity.x > 0:
        self.velocity.x = max(0, self.velocity.x - self.velocity_decrement)
      elif self.velocity.x < 0:
        self.velocity.x = min(0, self.velocity.x + self.velocity_decrement)
      self.acceleration.x = max(1, self.acceleration.x - self.acceleration_decrement)

    if (self.rect.left - self.movement_clamp < 0 and self.velocity.x < 0):
      self.velocity.x = 0
      self.acceleration.x = 1
    elif (self.rect.left > self.game.display.get_size()[0] - self.width - self.movement_clamp and self.velocity.x > 0):
      self.velocity.x = 0
      self.acceleration.x = 1

    self.rect.move_ip(self.velocity.x * self.acceleration.x, self.velocity.y * self.acceleration.y)

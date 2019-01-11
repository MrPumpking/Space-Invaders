from stars import Stars
from player import Player
from pygame import Surface

class GameScreen(Surface):
  def __init__(self, game):
    Surface.__init__(self, game.display.get_size())
    self.convert()
    self.game = game
    self.projectiles = []

    self.stars = Stars(self.game, 250)
    
    self.player = Player(self)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

  def update(self):
    self.player.update()
    self.stars.update()
    
    for projectile in self.projectiles:
      projectile.update()

      if projectile.rect.top + projectile.rect.height < 0 or projectile.rect.top > self.game.get_height():
        self.projectiles.remove(projectile)
        projectile.kill()

  def render(self):
    self.fill((19, 15, 64))
    self.stars.render(self)

    for projectile in self.projectiles:
      projectile.render(self)

    self.player.render(self)
from stars import Stars
from player import Player
from pygame import Surface

class GameScreen(Surface):
  def __init__(self, game):
    Surface.__init__(self, game.display.get_size())
    self.convert()
    self.game = game

    self.stars = Stars(self.game)
    
    self.player = Player(self.game)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

  def update(self):
    self.player.update()

  def render(self):
    self.fill((19, 15, 64))
    self.blit(self.stars, (0, 0))
    self.blit(self.player.sprite, self.player.rect)

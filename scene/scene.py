from pygame.surface import Surface

class Scene(Surface):
  def __init__(self, game, size):
    super().__init__(self, size)

    self.game = game
    self.size = size
    self.convert_alpha()

  def update(self):
    pass

  def render(self):
    pass

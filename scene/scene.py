from pygame.surface import Surface

class Scene(Surface):
  def __init__(self, game, size):
    super().__init__(size)

    self.game = game
    self.size = size
    self.convert_alpha()

  def render_group(self, group):
    for sprite in group.sprites():
      sprite.render(self)

  def update(self):
    pass

  def render(self):
    pass

  def kill(self):
    pass

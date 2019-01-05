from pygame import Surface, SRCALPHA

class Stars(Surface):
  def __init__(self, game):
    Surface.__init__(self, (game.get_width(), game.get_height()), SRCALPHA, 32)
    self.convert_alpha()
    self.generate_star(100, 100, 1)

  def generate_star(self, x, y, size = 100):
    size_half = int(size / 2)

    self.fill((255, 0, 255), (x - size_half, y - size_half, size, size))
    self.set_at((x, y), (0, 255, 255))

    for yPos in range(y - size_half, y + size_half):
      self.set_at((x, yPos), (255, 255, 255))
    for xPos in range(x - size_half, x + size_half):
      self.set_at((xPos, y), (255, 255, 255))

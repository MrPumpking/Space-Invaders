from entity.enemy import Enemy

class Dove(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "dove.png", 1, 10, 10)
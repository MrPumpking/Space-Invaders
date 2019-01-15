from entity.enemy import Enemy

class Ninja(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ninja.png", 1, 10)
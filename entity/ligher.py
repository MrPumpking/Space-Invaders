from entity.enemy import Enemy

class Ligher(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ligher.png", 2, 30)
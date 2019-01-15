from entity.enemy import Enemy

class Ligher(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ligher.png", health=2, points=25, weapon_power=5)
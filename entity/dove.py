from entity.enemy import Enemy

class Dove(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "dove.png", health=1, points=10, weapon_power=10)
from entity.enemy import Enemy

class Ninja(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ninja.png", health=3, points=50, weapon_power=5)
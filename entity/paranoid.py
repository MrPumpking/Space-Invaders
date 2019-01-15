from entity.enemy import Enemy

class Paranoid(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "Paranoid.png", health=4, points=100, weapon_power=10)
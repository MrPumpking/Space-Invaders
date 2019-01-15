from entity.enemy import Enemy

class UFO(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ufo.png", health=3, points=75, weapon_power=15)
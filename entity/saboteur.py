from entity.enemy import Enemy

class Saboteur(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "saboteur.png", health=5, points=200, weapon_power=25)
from entity.enemy import Enemy

class Saboteur(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "saboteur.png", 5, 100)
from entity.enemy import Enemy

class UFO(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "ufo.png", 6, 150)
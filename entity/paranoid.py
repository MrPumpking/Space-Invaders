from entity.enemy import Enemy

class Paranoid(Enemy):
  def __init__(self, screen):
    super().__init__(screen, "Paranoid.png", 4, 80)
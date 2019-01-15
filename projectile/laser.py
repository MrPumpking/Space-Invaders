from projectile.projectile import Projectile

class Laser(Projectile):
  def __init__(self, source_pos, direction = -1, power = 1):
    super().__init__("laser.png", direction)
    spawn_x = source_pos.left + (source_pos.width / 2) - (self.rect.width // (2 * self.scale))
    self.power = power
    self.rect.move_ip(spawn_x, source_pos.top)

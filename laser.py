import projectile

class Laser(projectile.Projectile):
  def __init__(self, player_pos, direction = -1):
    super().__init__("laser.png", direction)
  
    spawn_x = player_pos.left + (player_pos.width / 2) - (self.rect.width // (2 * self.scale))
    self.rect.move_ip(spawn_x, player_pos.top)
from animated_sprite import AnimatedSprite

class Actor(AnimatedSprite):
  def __init__(self):
    super().__init__(self, self, image_path, sprite_size, frames = 1, scale = 1, animation_speed = 10, start_frame = 0):

  def move(x, y):
    self.rect.move_ip(x, y)

  def update(self):
    pass

  def render(self, scene):
    scene.blit(self.sprite, self.rect)
  
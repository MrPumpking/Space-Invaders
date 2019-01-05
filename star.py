from animated_sprite import AnimatedSprite

class Star(AnimatedSprite):
  def __init__(self, animation_speed, start_frame):
    AnimatedSprite.__init__(self, "star.png", 5, 8, 3, animation_speed, start_frame)
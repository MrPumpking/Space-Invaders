from graphics.star import Star
from util.timer import Timer
from random import randint, seed
from pygame import Surface, SRCALPHA

class Stars(Surface):
  def __init__(self, scene, amount, spawn_chance = 50, animated_spawn_chance = 10, scale = (1, 3), alpha_range = (50, 100)):
    super().__init__((scene.game.get_width(), scene.game.get_height()), SRCALPHA, 32)
    seed()

    self.convert_alpha()
    self.scene = scene
    self.game = scene.game
    self.stars = []
    self.scroll = 100
    self.parallax_scroll = 0
    self.timer = Timer()
    self.timer2 = Timer()

    for _ in range(amount):
      if randint(0, 100) < spawn_chance:
        coords = self.get_random_coords()

        if (randint(0, 100) < animated_spawn_chance):
          star = Star(150, randint(0, 8))
          star.rect.move_ip(coords[0], coords[1])
          self.stars.append(star)
        else:
          self.generate_star(coords[0], coords[1], randint(scale[0], scale[1]), (255, 255, 255, randint(alpha_range[0], alpha_range[1])))
    
  def get_random_coords(self):
    return (randint(0, self.game.get_width()), randint(0, self.game.get_height()))

  def generate_star(self, x, y, scale = 3, color = (255, 255, 255, 255)):
    scale = scale if scale % 2 != 0 else scale + 1
    scale_half = scale // 2

    for yPos in range (y - scale_half, y + scale_half + 1):
      for xPos in range(x - scale_half, x + scale_half + 1):
        self.set_at((xPos, yPos), color)

  def update(self):
    if self.timer.has_passed(80):
      self.scroll += 1

    if self.timer2.has_passed(0.5):
      self.parallax_scroll += 1

    if self.scroll > self.game.get_height():
      self.scroll = 0

    if self.parallax_scroll > self.game.get_height():
      self.parallax_scroll = 0

    for star in self.stars:
      star.update()

  def render(self):
    self.scene.blit(self, (0, self.scroll), (0, 0, self.game.get_width(), self.game.get_height() - self.scroll))
    self.scene.blit(self, (0, 0), (0, self.game.get_height() - self.scroll, self.game.get_width(), self.scroll))
    
    for star in self.stars:
      y = star.rect.top
      coords = (
        star.rect.left,
        abs(self.game.get_height() - y - self.parallax_scroll) if y + self.parallax_scroll > self.game.get_height() else y + self.parallax_scroll)
      star.render(self.scene, coords)


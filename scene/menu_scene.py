from scene.scene import scene

'''
http://www.thorpy.org/index.html
'''
class MenuScene(Scene):
  def __init__(self, game):
    super().__init__(game, game.display.get_size())

  def render(self):
    pass

  def update(self):
    pass

  def kill(self):
    pass
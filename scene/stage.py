class Stage():
  def __init__(self):
    self.active_scene = None

  def set_active_scene(self, scene):
    if self.active_scene != None:
      self.active_scene.kill()
    self.active_scene = scene

  def get_active_scene(self):
    return self.active_scene
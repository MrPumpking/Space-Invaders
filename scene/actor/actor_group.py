from pygame.sprite import Group

class ActorGroup(Group):
  def __init__(self, *actors):
    super().__init__(self, actors)

  def render(self, scene):
    for actor in self.sprites
      actor.render(scene)
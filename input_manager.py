from pygame.locals import *

class InputManager():
  def __init__(self):
    self.keys = {}

  def update(self, event):
    if event.type == KEYDOWN:
      self.keys[event.key] = 1
    elif event.type == KEYUP:
      self.keys[event.key] = 0

  def key(self, key):
    return key in self.keys and self.keys[key]
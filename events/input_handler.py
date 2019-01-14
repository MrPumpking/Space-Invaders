from pygame.locals import KEYDOWN, KEYUP

class InputHandler():
  def __init__(self, event_manager):
    self._keys = {}
    self._events = event_manager
    self._events.register_listener(KEYUP, self.__on_key_up)
    self._events.register_listener(KEYDOWN, self.__on_key_down)

  def __on_key_up(self, event):
    self._keys[event.key] = False

  def __on_key_down(self, event):
    self._keys[event.key] = True

  def key(self, key):
    return key in self._keys and self._keys[key]
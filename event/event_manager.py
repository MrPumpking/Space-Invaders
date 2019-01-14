from pygame.locals import USEREVENT

class EventManager():
  def __init__(self):
    self._listeners = {}

  def register_listener(self, event, handler):
    if event in self._listeners:
      self._listeners[event].append(handler)
    else:
      self._listeners[event] = [handler]

  def unregister_listener(self, event, handler):
    if event in self._listeners:
      self._listeners[event].remove(handler)

  def handle(self, event):
    key = event.name if event.type == USEREVENT else event.type

    if not key in self._listeners:
      return

    for listener in self._listeners[key]:
      listener(event)
    
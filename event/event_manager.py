from pygame.locals import USEREVENT
from pygame.event import post, Event

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
    key = event._name if event.type == USEREVENT else event.type

    if not key in self._listeners:
      return

    for listener in self._listeners[key]:
      listener(event)

  def broadcast(self, event_type, event_values):
    real_type = USEREVENT if type(event_type) == str else event_type

    if real_type == USEREVENT:
      event_values['_name'] = event_type 

    event = Event(real_type, event_values)
    post(event)

import pygame
from pygame.locals import *
from scene.game_scene import GameScene
from event.event_manager import EventManager
from event.input_handler import InputHandler

class Game():
  def __init__(self):
    self.events = EventManager()
    self.display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Baby")
    # pygame.mouse.set_visible(0)

    self.input = InputHandler(self.events)
    self.current_scene = GameScene(self)
  
  def get_width(self):
    return self.display.get_size()[0]

  def get_height(self):
    return self.display.get_size()[1]

  def handle_event(self, event):
    self.events.handle(event)

  def update(self):
    self.current_scene.update()

  def render(self):
    self.current_scene.render()
    self.display.blit(self.current_scene, (0, 0))
    pygame.display.flip()
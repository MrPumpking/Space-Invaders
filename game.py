import pygame
from pygame.locals import *
from scene.stage import Stage
from scene.game_scene import GameScene
from event.event_manager import EventManager
from event.input_handler import InputHandler
from util.resources import load_music

class Game():
  def __init__(self):
    self.events = EventManager()
    self.display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Space Invaders")
    # pygame.mouse.set_visible(0)

    self.input = InputHandler(self.events)
    self.stage = Stage()
    self.stage.set_active_scene(GameScene(self))
    
    load_music('loop.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
  
  def get_width(self):
    return self.display.get_size()[0]

  def get_height(self):
    return self.display.get_size()[1]

  def handle_event(self, event):
    self.events.handle(event)

  def update(self):
    self.stage.get_active_scene().update()

  def render(self):
    self.stage.get_active_scene().render()
    self.display.blit(self.stage.get_active_scene(), (0, 0))
    pygame.display.flip()
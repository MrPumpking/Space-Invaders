import pygame
from player import Player
from pygame.locals import *
from game_screen import GameScreen
from input_manager import InputManager

class Game():
  def __init__(self):
    self.display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Baby")
    # pygame.mouse.set_visible(0)

    self.input = InputManager()
    self.current_screen = GameScreen(self)
  
  def get_width(self):
    return self.display.get_size()[0]

  def get_height(self):
    return self.display.get_size()[1]

  def handle_event(self, event):
    self.input.update(event)

  def update(self):
    self.current_screen.update()

  def render(self):
    self.current_screen.render()
    self.display.blit(self.current_screen, (0, 0))
    pygame.display.flip()
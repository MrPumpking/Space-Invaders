import os
import pygame
from game import Game
from pygame.locals import *

def main():
  os.environ['SDL_VIDEO_CENTERED'] = '1'
  pygame.init()
  game = Game()
  clock = pygame.time.Clock()

  while True:
    clock.tick(60)

    for event in pygame.event.get():
      if event.type == QUIT:
        return
      else:
        game.handle_event(event)

    game.update()
    game.render()

if __name__ == '__main__':
  main()


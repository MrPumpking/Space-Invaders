import os
import pygame

working_dir = os.path.dirname(os.path.realpath(__file__))

def load_image(name):
  fullname = os.path.join(working_dir, 'assets', name)

  try:
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
      image = image.convert()
    else:
      image = image.convert_alpha()
  except pygame.error:
    print('Cannot load image: {}'.format(fullname))
    raise SystemExit
  return image, image.get_rect()
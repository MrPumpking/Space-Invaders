import os
import sys
import pygame

working_dir = os.path.dirname(sys.modules['__main__'].__file__)

def get_asset_path(name):
  return os.path.join(working_dir, 'assets', name)

def load_image(name, scale = 1, alpha = True):
  fullname = get_asset_path(name)

  try:
    image = pygame.image.load(fullname)
    if not alpha or image.get_alpha() is None:
      image = image.convert()
    else:
      image = image.convert_alpha()
  except pygame.error:
    print('Cannot load image: {}'.format(fullname))
    raise SystemExit
  image = pygame.transform.scale(image, (image.get_rect().width * scale, image.get_rect().height * scale))
  rect = image.get_rect()
  rect.width, rect.height = rect.width * scale, rect.height * scale
  return image, rect
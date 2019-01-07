import os
import pygame

working_dir = os.path.dirname(os.path.realpath(__file__))

def load_image(name, scale = 1):
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
  image = pygame.transform.scale(image, (image.get_rect().width * scale, image.get_rect().height * scale))
  rect = image.get_rect()
  rect.width, rect.height = rect.width * scale, rect.height * scale
  return image, rect
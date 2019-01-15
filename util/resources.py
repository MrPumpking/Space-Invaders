import os
import sys
import pygame

working_dir = os.path.dirname(sys.modules['__main__'].__file__)

def get_asset_path(name):
  return os.path.join(working_dir, 'assets', name)

def load_image(name, scale = 1, alpha = True, width = 0, height = 0):
  fullname = get_asset_path(name)

  try:
    image = pygame.image.load(fullname)
    if not alpha or image.get_alpha() is None:
      image = image.convert()
    else:
      image = image.convert_alpha()
  except pygame.error:
    print('Could not load image: {}'.format(fullname))
    raise SystemExit

  width = max(width, image.get_rect().width * scale)
  height = max(height, image.get_rect().height * scale)
  image = pygame.transform.scale(image, (width, height))
  rect = image.get_rect()
  rect.width, rect.height = rect.width * scale, rect.height * scale
  return image, rect

def load_music(path):
  try:
    pygame.mixer.music.load(os.path.join(working_dir, 'assets', 'audio', path))
  except pygame.error:
    print('Could not load music file {}'.format(path))

def load_sound(path):
  try:
    return pygame.mixer.Sound(os.path.join(working_dir, 'assets', 'audio', path))
  except pygame.error:
    print('Could not load sound file {}'.format(path))

def write_to_file(path, value):
  f = open(os.path.join(working_dir, 'data', path), 'a')
  f.write(value + '\n')
  f.close()
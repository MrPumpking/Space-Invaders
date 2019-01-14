from stars import Stars
from enemy import Enemy
from player import Player
from pygame import Surface
from pygame.sprite import Group, groupcollide

class GameScreen(Surface):
  def __init__(self, game):
    Surface.__init__(self, game.display.get_size())
    self.convert()
    self.game = game
    self.enemies = Group()
    self.projectiles = Group()

    self.stars = Stars(self.game, 250)
    
    self.player = Player(self)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

    enemy1 = Enemy(self, "UFO.png")
    enemy1.rect.move_ip(0, 0)
    enemy2 = Enemy(self, "UFO.png")
    enemy2.rect.move_ip(1 * 3 * 32, 0)
    enemy3 = Enemy(self, "UFO.png")
    enemy3.rect.move_ip(2 * 3 * 32, 0)
    enemy4 = Enemy(self, "UFO.png")
    enemy4.rect.move_ip(3 * 3 * 32, 0)
    enemy5 = Enemy(self, "UFO.png")
    enemy5.rect.move_ip(4 * 3 * 32, 0)

    self.enemies.add(enemy1, enemy2, enemy3, enemy4, enemy4, enemy5)

  def handle_collisions(self):
    collisions = groupcollide(self.enemies, self.projectiles, False, False)
    print(collisions)

  def update(self):
    self.player.update()
    self.stars.update()
    self.projectiles.update()
    self.enemies.update()

    for projectile in self.projectiles:
      if projectile.rect.top + projectile.rect.height < 0 or projectile.rect.top > self.game.get_height():
        projectile.kill()

    self.handle_collisions()

  def render(self):
    self.fill((19, 15, 64))
    self.stars.render(self)

    for projectile in self.projectiles:
      projectile.render(self)

    for enemy in self.enemies:
      enemy.render(self)

    self.player.render(self)
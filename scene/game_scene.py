from scene.scene import Scene
from graphics.stars import Stars
from entity.player import Player
from entity.enemy import Enemy
from pygame.sprite import Group, groupcollide, spritecollide

class GameScene(Scene):
  def __init__(self, game):
    super().__init__(game, game.display.get_size())

    self.background = Stars(self, 250)
    self.player = Player(self)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

    self.enemies = Group()
    self.projectiles = Group()

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

    self.enemies.add(enemy1, enemy2, enemy3, enemy4, enemy5)

  def handle_collisions(self):
    hit = groupcollide(self.projectiles, self.enemies, True, False)
    
    for _, enemies in hit.items():
      for enemy in enemies:
        enemy.hit(self.player.weapon_power)

  def update(self):
    self.background.update()
    self.projectiles.update()
    self.enemies.update()
    self.player.update()
    self.handle_collisions()

  def render(self):
    self.fill((19, 15, 64))    
    self.background.render()
    self.render_group(self.projectiles)
    self.render_group(self.enemies)
    self.player.render(self)
  
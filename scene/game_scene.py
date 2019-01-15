from scene.scene import Scene
from graphics.stars import Stars
from entity.player import Player
from entity.enemy import Enemy
from pygame.sprite import Group, groupcollide, spritecollide
from pygame.font import Font
from util.resources import get_asset_path
from entity.swarm import Swarm
from itertools import chain

class GameScene(Scene):
  def __init__(self, game):
    super().__init__(game, game.display.get_size())
    self.game.events.register_listener('ENEMY_KILLED', self.increase_score)
    self.game.events.register_listener('PLAYER_HEALTH_UPDATE', self.write_health)

    self.background = Stars(self, 250)
    self.player = Player(self)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

    self.enemies = Group()
    self.projectiles = Group()
    self.enemy_projectiles = Group()
    self.score = 0

    self.font = Font(get_asset_path('dpcomic.ttf'), 32)
    self.write_score()
    self.write_health()

    self.swarm = Swarm(self, "waves/1.png")
    self.swarm.spawn()
    self.enemies.add(self.swarm.ships)

  def write_score(self):
    self.text_score = self.font.render('Score: {}'.format(self.score), False, (255, 255, 255))
    self.text_score_shadow = self.font.render('Score: {}'.format(self.score), False, (7, 5, 23))

  def write_health(self, event = None):
    self.text_health = self.font.render('Health: {}'.format(self.player.health), False, (255, 255, 255))
    self.text_health_shadow = self.font.render('Health: {}'.format(self.player.health), False, (7, 5, 23))

  def increase_score(self, event):
    self.score += event.points
    self.write_score()

  def handle_collisions(self):
    hit = groupcollide(self.projectiles, self.enemies, True, False)
    
    for _, enemies in hit.items():
      for enemy in enemies:
        if enemy.hit(self.player.weapon_power):
          self.swarm.on_ship_destroyed(enemy)

    player_hit = spritecollide(self.player, self.enemy_projectiles, True)
    
    if len(player_hit) > 0:
      self.game.events.broadcast('PLAYER_HIT', { 'damage': player_hit[0].power })

  def handle_projectiles(self):
    for projectile in chain(self.projectiles, self.enemy_projectiles):
      if projectile.rect.top + projectile.rect.height < 0 or projectile.rect.top > self.game.get_height():
        projectile.kill()

  def update(self):
    self.background.update()
    self.projectiles.update()
    self.enemy_projectiles.update()
    self.enemies.update()
    self.player.update()
    self.handle_collisions()
    self.handle_projectiles()
    self.swarm.update()

  def render_text_with_outline(self, text, text_shadow, x, y, outline = 3):
    self.blit(text_shadow, (x - outline, y))
    self.blit(text_shadow, (x + outline, y))
    self.blit(text_shadow, (x, y - outline))
    self.blit(text_shadow, (x, y + outline))
    self.blit(text, (x, y))

  def render(self):
    self.fill((19, 15, 64))    
    self.background.render()
    self.render_group(self.projectiles)
    self.render_group(self.enemy_projectiles)
    self.render_group(self.enemies)
    self.player.render(self)

    self.render_text_with_outline(
      self.text_score, self.text_score_shadow,
      self.game.get_width() - self.text_score.get_rect().width - 16,
      self.game.get_height() - self.text_score.get_rect().height - 16)

    self.render_text_with_outline(
      self.text_health, self.text_health_shadow,
      16, self.game.get_height() - self.text_health.get_rect().height - 16)

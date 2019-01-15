from scene.scene import Scene
from graphics.stars import Stars
from entity.player import Player
from entity.enemy import Enemy
from pygame.sprite import Group, groupcollide, spritecollide
from pygame.font import Font
from entity.swarm import Swarm
from itertools import chain
from util.resources import *
from util.timer import Timer
import datetime

class GameScene(Scene):
  def __init__(self, game):
    super().__init__(game, game.display.get_size())
    self.game.events.register_listener('ENEMY_KILLED', self.increase_score)
    self.game.events.register_listener('SWARM_DESTROYED', self.on_swarm_destroyed)
    self.game.events.register_listener('PLAYER_HEALTH_UPDATE', self.write_health)
    self.game.events.register_listener('PLAYER_DESTROYED', self.on_player_destroyed)

    self.background = Stars(self, 250)
    self.player = Player(self)
    self.player.rect.move_ip(
      self.game.display.get_size()[0] / 2 - self.player.rect.width / 2,
      self.game.display.get_size()[1] - self.player.rect.height - 20)

    self.enemies = Group()
    self.projectiles = Group()
    self.enemy_projectiles = Group()
    self.score = 0

    self.game_over = False
    self.show_overlay = False

    self.font = Font(get_asset_path('dpcomic.ttf'), 32)
    self.write_score()
    self.write_health()

    self.laser_sound = load_sound('laser.ogg')
    self.laser_sound.set_volume(0.2)
    
    self.waves = [
      Swarm(self, 'waves/1.png'),
      Swarm(self, 'waves/2.png'),
      Swarm(self, 'waves/3.png')
    ]

    self.spawn_timer = Timer()
    self.current_wave_id = 1
    self.current_wave = self.waves.pop(0)
    self.current_wave_active = False
    self.spawn_swarm(self.current_wave)

    self.overlay, _ = load_image('overlay.png', width=self.game.get_width(), height=self.game.get_height())

  def spawn_swarm(self, swarm):
    swarm.ships.clear()
    swarm.spawn()
    self.enemies.add(self.current_wave.ships)  
    self.spawn_timer.restart()
    self.write_overlay('Wave {}'.format(self.current_wave_id))

  def spawn_projectile(self, group, projectile):
    group.add(projectile)
    self.laser_sound.play()

  def write_score(self):
    self.text_score = self.font.render('Score: {}'.format(self.score), False, (255, 255, 255))
    self.text_score_shadow = self.font.render('Score: {}'.format(self.score), False, (7, 5, 23))

  def write_score_to_file(self):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    write_to_file('scores.txt', "{} = {}".format(time, self.score))

  def write_health(self, event = None):
    self.text_health = self.font.render('Health: {}'.format(self.player.health), False, (255, 255, 255))
    self.text_health_shadow = self.font.render('Health: {}'.format(self.player.health), False, (7, 5, 23))

  def write_overlay(self, text):
    self.show_overlay = True
    self.text_gameover = self.font.render(text, False, (255, 255, 255))
    self.text_gameover_shadow = self.font.render(text, False, (7, 5, 23))

  def increase_score(self, event):
    self.score += event.points
    self.write_score()

  def on_swarm_destroyed(self, event):
    self.current_wave_active = False

    if len(self.waves) == 0:
      self.write_overlay('Victory!')
      self.write_score_to_file()
      self.game_over = True
    else:
      self.current_wave_id += 1
      self.current_wave = self.waves.pop(0)
      self.spawn_swarm(self.current_wave)

  def on_player_destroyed(self, event):
    if self.game_over:
      return

    self.game_over = True
    self.write_overlay('Game Over!')
    self.write_score_to_file()
    self.player.kill()

  def handle_collisions(self):
    hit = groupcollide(self.projectiles, self.enemies, True, False)
    
    for _, enemies in hit.items():
      for enemy in enemies:
        if enemy.hit(self.player.weapon_power):
          self.current_wave.on_ship_destroyed(enemy)

    player_hit = spritecollide(self.player, self.enemy_projectiles, True)
    
    if len(player_hit) > 0:
      self.game.events.broadcast('PLAYER_HIT', { 'damage': player_hit[0].power })

  def handle_projectiles(self):
    for projectile in chain(self.projectiles, self.enemy_projectiles):
      if projectile.rect.top + projectile.rect.height < 0 or projectile.rect.top > self.game.get_height():
        projectile.kill()

  def update(self):
    if self.spawn_timer.has_passed_once(1500):
      self.current_wave_active = True
      self.show_overlay = False

    self.background.update()
    
    if self.current_wave_active:
      self.projectiles.update()
      self.enemy_projectiles.update()
      self.enemies.update()

    if not self.game_over:
      self.player.update()
      self.handle_projectiles()

    self.handle_collisions()
    self.current_wave.update()
    
    if self.current_wave.rect.top + self.current_wave.rect.height >= self.player.rect.top + 10:
      self.game.events.broadcast('PLAYER_DESTROYED', {})

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
    
    if self.current_wave_active:
      self.render_group(self.enemy_projectiles)
      self.render_group(self.enemies)
    
    if not self.game_over:
      self.player.render(self)

    if self.show_overlay:
      self.blit(self.overlay, (0, 0))
      self.render_text_with_outline(
        self.text_gameover, self.text_gameover_shadow,
        self.game.get_width() / 2 - self.text_gameover.get_rect().width / 2,
        self.game.get_height() / 2 - self.text_gameover.get_rect().height / 2
      )

    self.render_text_with_outline(
      self.text_score, self.text_score_shadow,
      self.game.get_width() - self.text_score.get_rect().width - 16,
      self.game.get_height() - self.text_score.get_rect().height - 16)

    self.render_text_with_outline(
      self.text_health, self.text_health_shadow,
      16, self.game.get_height() - self.text_health.get_rect().height - 16)

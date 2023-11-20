import math

import pygame
import random


class Shape(pygame.sprite.Sprite):
    def __init__(self, img, pos, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.life = life


class Fly(Shape):
    def __init__(self, img, pos, life):
        super().__init__(img, pos, life)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.size = (100, 100)

    def update(self):
        self.rect.x -= 1
        if self.rect.x < -500:
            self.kill()

    def shoot(self, img):
        x, y = self.rect.center
        bullet = BulletAliens(img, (x + 180, y + 200), color='green')
        return bullet


class CircleMotion(Shape):
    def __init__(self, img, pos, life):
        super().__init__(img, pos, life)
        self.x = pos[0]
        self.y = pos[1]
        self.time = 0
        self.radius = 300
        self.omega = 0.01
        # self.image.fill('red',special_flags=pygame.BLEND_RGB_MIN)

    def update(self):
        self.time += 0.007

        x = self.x + (self.radius * math.cos(self.time))
        y = self.y - (self.radius * math.sin(self.time))
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class settings:
    def __init__(self, width=1900, height=1050):
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.width = width
        self.height = height
        self.pos_spaceship = pygame.Vector2(self.width / 2, 900)
        self.image_fly = 'fly.png'
        self.image_spaceship = "ship.bmp"
        self.image_alien = 'alien.bmp'
        self.image_bullet = "bullet.png"
        self.start = pygame.image.load('start.bmp')
        self.next = pygame.image.load('next step.bmp')
        self.game_over = pygame.image.load('game over.bmp')
        self.bg = pygame.image.load('space.jpg')
        self.bg = pygame.transform.scale(self.bg, (1900, 1050))
        self.you_win = pygame.image.load('you win.jpg')


class Block(Shape):
    pass


class Board:
    def __init__(self):
        self.level = 1
        self.last_shoot_fly = 0
        self.settings = settings()
        self.score = 0
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.last_shoot_aliens = 0
        self.spaceship_group = pygame.sprite.Group()
        self.fly_group = pygame.sprite.Group()
        self.spaceship = SpaceShip(self.settings.image_spaceship, self.settings.pos_spaceship, 3)
        self.last_fly = 0

        # self.obj = CircleMotion(self.settings.image_alien, pygame.Vector2(800, 450), 3)
        # self.obj_g = pygame.sprite.Group()
        # self.obj_g.add(self.obj)

        self.bullet_spaceship_group = pygame.sprite.Group()
        self.bullet_aliens_group = pygame.sprite.Group()
        self.aliens_group = pygame.sprite.Group()

    def update(self):
        self.screen.blit(self.settings.bg, (0, 0))
        time_now = pygame.time.get_ticks()
        self.bullet_spaceship_group.update()
        self.bullet_aliens_group.update()
        self.fly_group.update()

        for alien in self.aliens_group:
            if alien.rect.left > 1800 or alien.rect.right < 100:
                self.aliens_group.update(0)
                break
        self.aliens_group.update(1)

        if self.aliens_group:
            x, y = random.choice(list(self.aliens_group)).rect.center
            if time_now - self.last_shoot_aliens > 450 or len(self.bullet_aliens_group) < 1:
                bullet = BulletAliens(self.settings.image_bullet, (x + 180, y + 200))
                self.bullet_aliens_group.add(bullet)
                self.last_shoot_aliens = time_now

        if time_now - self.last_fly > 10000 and self.level > 1:
            fly = Fly(self.settings.image_fly, (2000, 150), 1)
            self.fly_group.add(fly)
            self.last_fly = time_now

        for fly in self.fly_group:
            if time_now - self.last_shoot_fly > 500:
                self.bullet_aliens_group.add(fly.shoot(self.settings.image_bullet))
                self.last_shoot_fly = time_now

        score_text = self.settings.font.render(f'Score: {self.score}', True, 'gold')
        live_text = self.settings.font.render(f'live: {self.spaceship.life}', True, 'gold')
        munitions_text = self.settings.font.render(f'munitions: {self.spaceship.munitions}', True, 'gold')

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(live_text, (800, 10))
        self.screen.blit(munitions_text, (1500, 10))

        self.aliens_group.draw(self.screen)
        self.spaceship_group.draw(self.screen)
        self.bullet_spaceship_group.draw(self.screen)
        self.bullet_aliens_group.draw(self.screen)
        self.fly_group.draw(self.screen)
        # self.obj_g.update()
        # self.obj_g.draw(self.screen)

    def levels(self, level):
        if level == 1:
            for i in range(5):
                for j in range(7):
                    alien = Alien(self.settings.image_alien, (j * 120 + 50, i * 100 + 100), 0)
                    self.aliens_group.add(alien)
                    self.spaceship_group.add(self.spaceship)

        if level == 2:
            for i in range(5):
                for j in range(10):
                    alien = Alien(self.settings.image_alien, (j * 120 + 50, i * 100 + 200), 3)
                    self.aliens_group.add(alien)
                    self.spaceship_group.add(self.spaceship)
                    self.spaceship.munitions = 1000

    def clean(self):
        if self.spaceship_group:
            self.spaceship_group.empty()
        if self.aliens_group:
            self.aliens_group.empty()
        if self.bullet_aliens_group:
            self.bullet_aliens_group.empty()
        if self.bullet_spaceship_group:
            self.bullet_spaceship_group.empty()


class MainGame:
    def __init__(self):
        self.screen = Board()
        self.status = 'game start'
        self.running = True
        self.first_shoot = True
        self.last_shoot_spaceship = 0
        while self.running:

            self.screen.screen.fill("black")
            # self.screen.screen.blit(self.screen.settings.bg_image,(0,0))
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.status == 'game over':
                self.screen.screen.blit(self.screen.settings.game_over, (450, 0))
                if keys[pygame.K_RETURN]:
                    self.running = False

            if self.status == 'you win':
                self.screen.screen.blit(self.screen.settings.you_win, (450, 450))
                if keys[pygame.K_RETURN]:
                    self.running = False

            if self.status == 'game start':
                self.screen.screen.blit(self.screen.settings.start, (450, 0))
                if keys[pygame.K_RETURN]:
                    self.screen.levels(1)
                    self.status = 'run'

            if self.status == 'next step':
                self.screen.screen.blit(self.screen.settings.next, (450, 0))
                if keys[pygame.K_RETURN]:
                    self.screen.level += 1
                    self.screen.levels(self.screen.level)
                    self.status = 'run'

            if self.status == 'run':
                self.collision_check()
                self.screen.update()
                self.game_over()

                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # and self.rect.left > 0:
                    self.screen.spaceship.move(direction=1)
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # and self.rect.right < 1280:
                    self.screen.spaceship.move(direction=0)
                if keys[pygame.K_SPACE]:
                    self.shoot()

            pygame.display.update()

        self.good_bye()

        pygame.quit()

    def good_bye(self):
        game_over_text = self.screen.settings.font.render('good bye', True, 'gold')
        self.screen.screen.blit(game_over_text,
                                (self.screen.settings.width // 2 - 100, self.screen.settings.height // 2))
        pygame.display.flip()
        pygame.time.delay(1000)

    def collision_check(self):
        pygame.sprite.groupcollide(self.screen.bullet_spaceship_group, self.screen.bullet_aliens_group, True, True)
        if pygame.sprite.groupcollide(self.screen.bullet_spaceship_group, self.screen.fly_group, True, True):
            self.screen.score += 100
        if pygame.sprite.groupcollide(self.screen.spaceship_group, self.screen.aliens_group, True, False):
            self.screen.spaceship.life = 0
            self.game_over()
        if pygame.sprite.groupcollide(self.screen.spaceship_group, self.screen.bullet_aliens_group, False, True):
            self.screen.spaceship.life -= 1
            if self.screen.spaceship.life < 0:
                self.game_over()
        list_of_aliens = list(
            pygame.sprite.groupcollide(self.screen.aliens_group, self.screen.bullet_spaceship_group, False, True))
        for alien in list_of_aliens:
            self.screen.score += 20
            alien.was_shot()

    def shoot(self):
        time_now = pygame.time.get_ticks()
        if (time_now - self.last_shoot_spaceship > 100 or self.first_shoot) and len(
                self.screen.bullet_spaceship_group) < 300 and self.screen.spaceship.munitions > 0:
            self.screen.bullet_spaceship_group.add(self.screen.spaceship.shoot(self.screen.settings.image_bullet))
            self.screen.spaceship.munitions -= 1
            self.last_shoot_spaceship = time_now
            self.first_shoot = False

    def game_over(self):
        if self.screen.spaceship.life < 0 or (
                self.screen.spaceship.munitions == 0 and len(self.screen.aliens_group) != 0):
            self.status = 'game over'
        if len(self.screen.aliens_group) == 0 :
            self.screen.clean()
            if self.screen.level >= 2:
                self.status = 'you win'
            else:
                self.status = 'next step'


class SpaceShip(Shape):

    def __init__(self, img, pos, life, munitions=float('inf')):
        super().__init__(img, pos, life)
        self.last_shoot = 0
        self.munitions = munitions

    def move(self, direction: bool):
        if direction == 1 and self.rect.right < 1900:
            self.rect.x += 2
        if direction == 0 and self.rect.left > 0:
            self.rect.x -= 2

    def shoot(self, img):
        bullet = BulletSpaceShip(img, (self.rect.x + 203, self.rect.bottom + 85))
        return bullet


class Alien(SpaceShip):
    def __init__(self, img, pos, life):
        super().__init__(img, pos, life)
        self.speed = 1

    def update(self, direction):
        if direction:
            self.rect.x += self.speed
        else:
            self.rect.y += 10
            self.speed *= -1
        if self.rect.top > 1050:
            self.kill()

    def was_shot(self):
        if self.life != 0:
            self.life -= 1
            self.color()
        else:
            self.kill()

    def color(self):
        colors = {0: 'red', 2: 'yellow', 3: 'green', 1: 'orange'}
        self.image.fill(colors[self.life], special_flags=pygame.BLEND_RGB_MIN, )


class BulletSpaceShip(Shape):
    def __init__(self, img, pos, life=0):
        super().__init__(img, pos, life)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect.size = (10, 10)

    def update(self):
        self.rect.y -= 1
        if self.rect.bottom < 0 or self.rect.top > 1050:
            self.kill()


class BulletAliens(Shape):
    def __init__(self, img, pos, life=0, color='red'):
        super().__init__(img, pos, life)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect.size = (10, 10)
        self.image.fill(color, special_flags=pygame.BLEND_RGB_MIN, )

    def update(self):
        self.rect.y += 1
        if self.rect.bottom < 0 or self.rect.top > 1050:
            self.kill()


pygame.init()
main_game = MainGame()

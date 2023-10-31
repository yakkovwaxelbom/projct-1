import pygame
import random

spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

aliens_group = pygame.sprite.Group()


class Shape(pygame.sprite.Sprite):
    def __init__(self, img, pos, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.life = life

    def life(self):
        if self.life > 1:
            self.life -= 1
        else:
            self.kill()


class Spaceship(Shape):

    def __init__(self, img, pos, life):
        super().__init__(img, pos, life)
        self.last_shoot = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.rect.top > 0:
            self.rect.y -= 3
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.rect.bottom < 720:
            self.rect.y += 3
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= 3
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < 1280:
            self.rect.x += 3

        time_now = pygame.time.get_ticks()

        if keys[pygame.K_f] and time_now - self.last_shoot > 500:
            bullet = Bullet("ship.bmp", (self.rect.x, self.rect.top), 1, -1)
            bullet_group.add(bullet)
            self.last_shoot = time_now


class Bullet(Shape):
    def __init__(self, img, pos, life, direction):
        super().__init__(img, pos, life)
        self.direction = direction

    def move(self):
        self.rect.y += self.direction
        if self.rect.bottom < 0 or self.rect.top > 720:
            self.kill()


class Alien(Spaceship):
    def __init__(self, img, pos, life):
        super().__init__(img, pos, life)
        self.direction = 10

    def move(self):
        for alien in aliens_group:
            if 0 >= alien.rect.right or 1280 <= alien.rect.left:
                self.rect.y += 10
                self.direction *= -1
        self.rect.x += self.direction


# class Aliens:
#     def __init__(self):
#         self.last_shoot = 0
#         for i in range(4):
#             for j in range(6):
#                 alien = Alien('alien.bmp', (j * 120 + 500, i * 100 + 100), 1)
#                 aliens_group.add(alien)
#
#     def move(self):
#         for alien in aliens_group:
#             alien.move()
#         time_now = pygame.time.get_ticks()
#         x, y = random.choice(list(aliens_group)).rect.center
#         if time_now - self.last_shoot > 500:
#             print((x, y))
#             bullet = Bullet("ship.bmp", (x, y), 1, 1)
#             bullet_group.add(bullet)
#             self.last_shoot = time_now


pygame.init()
screen = pygame.display.set_mode((1280, 720))
spaceship = Spaceship("ship.bmp", pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 10)
spaceship_group.add(spaceship)
for i in range(5):
    for j in range(5):
        alien = Alien('alien.bmp', (j * 120 + 50, i * 100 + 100), 1)
        aliens_group.add(alien)
# shoot = Shoot()
# aliens = Aliens()
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    # shoot.shoot()
    spaceship.move()
    for bullet in bullet_group:
        bullet.move()
    # aliens.move()
    # aliens.shoot()
    for alien in aliens_group:
        alien.move()

    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    aliens_group.draw(screen)
    # aliens_group.draw(screen)

    pygame.display.update()

pygame.quit()
print(list(aliens_group)[7].rect)

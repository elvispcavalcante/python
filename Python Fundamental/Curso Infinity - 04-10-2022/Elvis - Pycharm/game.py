import random

from obj import Obj, Pipe, Coin, Bird, Text
import pygame


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()

        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)
        self.bird = Bird('assets/bird1.png', 50, 320, self.all_sprites)

        self.score = Text(100, '0')
        self.ticks = 0
        self.max_score = 0
        self.checa_score()
        self.change_scene = False

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score.draw(window, 160, 50)

    def updates(self):
        self.move_ground()
        self.move_bg()
        if self.bird.play:
            self.spaw_pipes()
            self.bird.collision_pipes(self.pipe_group)
            self.bird.collision_coins(self.coin_group)
            self.score.text_update(str(self.bird.pts))
            self.all_sprites.update()
        else:
            self.save_score()
            self.game_over()

    def move_ground(self):
        self.ground.rect[0] -= 2
        self.ground2.rect[0] -= 2
        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360

    def move_bg(self):
        self.bg.rect[0] -= 4
        self.bg2.rect[0] -= 4
        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 360

    def spaw_pipes(self):
        self.ticks += 1
        if self.ticks >= random.randint(60, 90):
            self.ticks = 0
            intervalo = random.randint(350, 500)

            pipe = Pipe("assets/pipe1.png", 400, intervalo, self.pipe_group, self.all_sprites)
            pipe2 = Pipe("assets/pipe2.png", 400, intervalo - 520, self.pipe_group, self.all_sprites)
            coin = Coin('assets/0.png', pipe.rect[0] + 28, pipe.rect[1] - 100, self.coin_group, self.all_sprites)

    def game_over(self):
        self.change_scene = True

    def checa_score(self):
        with open('score.txt', 'r') as file:
            self.max_score = int(file.read())

    def save_score(self):
        if self.bird.pts > self.max_score:
            with open('score.txt', 'w') as file:
                print(self.bird.pts)
                print(self.max_score)
                self.max_score = self.bird.pts
                file.write(str(self.max_score))
        # else:
        #         file.write(str(self.max_score))



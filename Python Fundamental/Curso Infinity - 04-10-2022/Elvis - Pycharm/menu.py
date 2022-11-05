import random

from obj import Obj, Pipe, Coin, Bird, Text
import pygame


class Menu:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        self.get_ready = Obj("assets/getready.png", 60, 100, self.all_sprites)
        self.table_score = Obj("assets/score.png", 20, 200, self.all_sprites)
        self.go = Obj("assets/go.png", 100, 420, self.all_sprites)

        self.score = Text(100, '0')
        self.change_scene = False
        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score.draw(window, 160, 260)

    def updates(self, pts):
        self.move_ground()
        self.move_bg()
        self.score.text_update(str(pts))
        self.all_sprites.update()

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

    def events(self, event):
        self.ticks += 1
        if event.type == pygame.MOUSEBUTTONUP:
            if self.go.rect.collidepoint(pygame.mouse.get_pos()):
                if self.ticks >= 10:
                    self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.change_scene = True

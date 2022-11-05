import pygame
from menu import Menu
from game import Game


class Main:
    def __init__(self):
        pygame.font.init()

        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("Flappy Bird")
        self.loop = True
        self.fps = pygame.time.Clock()
        self.game = Game()
        self.menu = Menu()

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.updates(str(self.game.max_score))
        elif not self.game.change_scene:
            self.game.updates()
            self.game.draw(self.window)
        else:
            self.loop = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
                print('Clicou no X')
            self.menu.events(event)

    def update(self):
        while self.loop:
            self.events()
            self.draw()
            self.fps.tick(30)
            pygame.display.update()

while True:
    Main().update()

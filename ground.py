import pygame
from pygame.sprite import Sprite


class Ground(Sprite):

    def __init__(self, main):

        super().__init__()
        self.screen = main.screen
        self.screen_width = main.screen_width
        self.screen_height = main.screen_height
        self.settings = main.settings

        self.width, self.height = self.screen_width, 5
        self.ground_color = pygame.Color(0, 162, 232, a=0)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):
        self.screen.fill(self.ground_color, self.rect)

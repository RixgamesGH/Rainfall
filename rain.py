from numpy import random
import pygame
from pygame.sprite import Sprite


class Rain(Sprite):

    def __init__(self, main):
        """Initialize the rain and its starting position"""
        super().__init__()
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings

        self.speed_multiplier = random.choice(self.settings.choices, p=self.settings.probability) * 0.1
        self.size_multiplier = round(self.speed_multiplier, 2)

        # Load in the image used for the rain
        self.image = pygame.image.load('images/rain.bmp')
        self.image = pygame.transform.scale(self.image, ((self.settings.scale / self.size_multiplier),
                                            (self.settings.scale * (217 / 126) / self.size_multiplier)))
        self.rect = self.image.get_rect()

        # Draw the raindrop to the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Get the exact position of the rain
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.layer = -self.size_multiplier

    def check_edges(self):
        """Check if the raindrops have moved off the screen"""
        return self.rect.top >= self.screen_rect.bottom

    def update(self):
        """Move the rain down"""
        self.y += self.settings.rain_speed * self.speed_multiplier
        self.rect.y = self.y

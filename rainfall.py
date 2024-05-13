import sys
import pygame
import random
from rain import Rain
from settings import Settings
from ground import Ground


class RainFall:

    def __init__(self):
        """Initialize game and game recourses"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Display the game on full screen and save the screen size in variables
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        print(self.screen.get_rect())

        # Make the game and make a caption for the game
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption("Rainfall")

        # Make a sprite group to save the raindrops in
        self.raindrops = pygame.sprite.LayeredUpdates()

        # Import ground class
        self.ground = Ground(self)
        self.ground_tiles = pygame.sprite.LayeredUpdates()
        self._draw_ground(0, self.screen_height)

        # Create the first drops for the rainfall
        self._create_rain_row()
        self.tick_count = 0

    def run_game(self):
        """The loop to run the game"""
        while True:
            self._check_events()
            if not self.tick_count % 6:
                self._create_rain_row()
            self._update_raindrops()
            self._update_screen()
            if self.tick_count == 0:
                pygame.display.flip()
            self.clock.tick(60)
            self.tick_count += 1
            print(len(self.raindrops))

    def _check_events(self):
        """Check for key inputs"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Apply changes upon certain key inputs"""
        if event.key == pygame.K_UP:
            if self.settings.rain_speed <= 20:
                self.settings.rain_speed += 1
        if event.key == pygame.K_DOWN:
            if self.settings.rain_speed > 5:
                self.settings.rain_speed -= 1
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _create_rain_row(self):
        """Create a horizontal row of raindrops"""
        raindrop_height = self.settings.scale * (217 / 126)
        raindrop_width = self.settings.scale

        current_x = 0
        current_y = raindrop_height * -0.5
        while current_x < (self.screen_width - raindrop_width):
            # Randomize chance to make a raindrop to make the rainfall more realistic
            chance = random.randint(0, 10)
            if chance == 1:
                self._create_raindrop(current_x, current_y)
            current_x += 0.4 * raindrop_width

    def _create_raindrop(self, x_position, y_position):
        """Create a new raindrop in given x and y coordinates"""
        new_raindrop = Rain(self)
        new_raindrop.x = x_position
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def _draw_ground(self, x_pos, y_pos):
        ground_tile = Ground(self)
        ground_tile.x = x_pos
        ground_tile.y = y_pos
        ground_tile.rect.x = x_pos
        ground_tile.rect.y = y_pos
        self.ground_tiles.add(ground_tile)

    def _check_rain_edges(self):
        """Check if rain has hit bottom of screen, then remove it"""
        pygame.sprite.groupcollide(self.ground_tiles, self.raindrops, False, True)

    def _update_raindrops(self):
        """Update the position of the raindrops"""
        self._check_rain_edges()
        self.raindrops.update()

    def _update_screen(self):
        """Update the screen and icons on the screen"""
        self.screen.fill(self.settings.bg_color)

        pygame.display.update(self.raindrops.draw(self.screen))

        
if __name__ == '__main__':
    """Run the game"""
    ai = RainFall()
    ai.run_game()

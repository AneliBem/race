import sys
import pygame

from settings import Settings

class Race:
    def __init__(self):
        pygame.init()
        
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        while True:
            self._check_events

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    ai = Race()
    ai.run_game()

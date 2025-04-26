import sys
import pygame

from settings import Settings
from car import Car

class Race:
    def __init__(self):
        pygame.init()
        
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.car = Car(self)

    def run_game(self):
        while True:
            self._check_events()
            self.car.update()
            self._update_screen()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.car.blitme()
  
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)           
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.car.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.car.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.car.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.car.moving_down = False


if __name__ == "__main__":
    ai = Race()
    ai.run_game()

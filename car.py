import pygame
from pygame.sprite import Sprite

class Car(Sprite):
    def __init__(self, ai_game):
        
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/car.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect.top > 0:
            self.rect.y -= self.settings.car_speed
        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.car_speed
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def position_car(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)
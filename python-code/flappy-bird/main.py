import pygame, sys
from settings import WIDTH, HEIGTH, ground_space
from world import World

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH + ground_space))
pygame.display.set_caption('Flappy Bird')

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('flappy-bird/flappy-bird-assets/bg.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGTH))
        self.ground_image = pygame.image.load('flappy-bird/flappy-bird-assets/ground.png')
        self.ground_scroll = 0
        self.scroll_speed = -6
        self.FPS = pygame.time.Clock()
        self.stop_ground_scroll = False

    

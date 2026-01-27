from os import walk
import pygame

WIDTH, HEIGTH = 600, 650

pipe_pair_size = [
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1)
]
pipe_size = HEIGTH // 10
pipe_gap = (pipe_size * 2) + (pipe_size // 2)
ground_space = 50

def import_assets(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
PACMAN_SIZE = 30
GHOST_SIZE = 30
PACMAN_SPEED = 5
GHOST_SPEED = 3
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Define the game grid (0 represents empty cell, 1 represents wall)
game_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Load images
pacman_img = pygame.image.load("images/pacman.png")
pacman_img = pygame.transform.scale(pacman_img, (PACMAN_SIZE, PACMAN_SIZE))
ghost_img = pygame.image.load("images/ghost.png")
ghost_img = pygame.transform.scale(ghost_img, (GHOST_SIZE, GHOST_SIZE))

# Set up game objects
pacman_x = SCREEN_WIDTH // 2 - PACMAN_SIZE // 2
pacman_y = SCREEN_HEIGHT // 2 - PACMAN_SIZE // 2
ghost_x = random.randint(0, SCREEN_WIDTH - GHOST_SIZE)
ghost_y = random.randint(0, SCREEN_HEIGHT - GHOST_SIZE)
pacman_dx = 0
pacman_dy = 0
ghost_dx = GHOST_SPEED
ghost_dy = GHOST_SPEED

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_dy = -PACMAN_SPEED
            elif event.key == pygame.K_DOWN:
                pacman_dy = PACMAN_SPEED
            elif event.key == pygame.K_LEFT:
                pacman_dx = -PACMAN_SPEED
            elif event.key == pygame.K_RIGHT:
                pacman_dx = PACMAN_SPEED

    # Move Pac-Man
    next_x = pacman_x + pacman_dx
    next_y = pacman_y + pacman_dy
    next_grid_x = next_x // BLOCK_SIZE
    next_grid_y = next_y // BLOCK_SIZE
    if 0 <= next_grid_y < len(game_grid) and 0 <= next_grid_x < len(game_grid[next_grid_y]):
        if not game_grid[next_grid_y][next_grid_x]:
            pacman_x = next_x
            pacman_y = next_y

    # Move ghost
    ghost_x += ghost_dx
    ghost_y += ghost_dy

    # Wrap around screen
    ghost_x = ghost_x % SCREEN_WIDTH
    ghost_y = ghost_y % SCREEN_HEIGHT

    # Draw walls
    for y in range(len(game_grid)):
        for x in range(len(game_grid[y])):
            if game_grid[y][x] == 1:
                pygame.draw.rect(screen, BLUE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw Pac-Man and Ghost
    screen.blit(pacman_img, (pacman_x, pacman_y))
    screen.blit(ghost_img, (ghost_x, ghost_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()

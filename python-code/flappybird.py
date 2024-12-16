import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIPE_WIDTH = 50
PIPE_GAP = 200
BIRD_SIZE = 30
BIRD_X = 100
BIRD_Y = SCREEN_HEIGHT // 2
GRAVITY = 0.25
FLAP_STRENGTH = -5
BACKGROUND_COLOR = (135, 206, 250)
PIPE_COLOR = (0, 128, 0)
BIRD_COLOR = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Define bird class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.vel_y = 0

    def flap(self):
        self.vel_y = FLAP_STRENGTH

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def draw(self):
        pygame.draw.circle(screen, BIRD_COLOR, (int(self.x), int(self.y)), BIRD_SIZE)

# Define pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height_top = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.height_bottom = SCREEN_HEIGHT - self.height_top - PIPE_GAP
        self.width = PIPE_WIDTH
        self.vel_x = -3

    def update(self):
        self.x += self.vel_x

    def draw(self):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, self.width, self.height_top))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, SCREEN_HEIGHT - self.height_bottom, self.width, self.height_bottom))

# Create bird and pipes
bird = Bird()
pipes = []

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update bird
    bird.update()

    # Generate pipes
    if len(pipes) == 0 or pipes[-1].x <= SCREEN_WIDTH - 200:
        pipes.append(Pipe())

    # Update pipes
    for pipe in pipes:
        pipe.update()

    # Remove off-screen pipes
    if pipes and pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)

    # Check for collisions with pipes or ground
    for pipe in pipes:
        if (bird.x + BIRD_SIZE > pipe.x and bird.x < pipe.x + PIPE_WIDTH and
                (bird.y < pipe.height_top or bird.y + BIRD_SIZE > SCREEN_HEIGHT - pipe.height_bottom)):
            running = False
    if bird.y < 0 or bird.y + BIRD_SIZE > SCREEN_HEIGHT:
        running = False

    # Draw bird and pipes
    bird.draw()
    for pipe in pipes:
        pipe.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

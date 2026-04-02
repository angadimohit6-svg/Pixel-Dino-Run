import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

dino_x = 60
dino_y = 30
dino_width = 10  
dino_height = 30
jump = False
jump_vel = 20

obstacle_width = 20
obstacle_height = 40
obstacle_x = WIDTH
obstacle_y = 200
speed = 6

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        dino_y -= jump_vel
        jump_vel -= 1
        if jump_vel < -10:
            jump = False
            jump_vel = 10
            dino_y = 200

    obstacle_x -= speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH + random.randint(0, 300)

    if (dino_x < obstacle_x + obstacle_width and
        dino_x + dino_width > obstacle_x and
        dino_y < obstacle_y + obstacle_height and
        dino_y + dino_height > obstacle_y):
        print("Game Over")
        running = False

    pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.update()

pygame.quit()
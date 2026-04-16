import pygame
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = Clock(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.update()

    pygame.display.flip()
    clock.tick(1)  # update every second

pygame.quit()
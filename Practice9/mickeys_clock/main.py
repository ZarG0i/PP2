import pygame
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")

fps_clock = pygame.time.Clock()
clock_ui = Clock(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock_ui.update()

    pygame.display.flip()
    fps_clock.tick(60)

pygame.quit()
import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 36)

playlist = [
    "C:/Users/ZANGAR/Desktop/Practice9/music_player/music/track1.wav.mp3",
    "C:/Users/ZANGAR/Desktop/Practice9/music_player/music/track2.wav.mp3"
]

player = Player(playlist)

running = True

while running:
    screen.fill((0, 0, 0))

    text = font.render("P=Play S=Stop N=Next B=Back Q=Quit", True, (255, 255, 255))
    track = font.render("Track: " + player.current_track(), True, (0, 255, 0))

    screen.blit(text, (20, 50))
    screen.blit(track, (20, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()
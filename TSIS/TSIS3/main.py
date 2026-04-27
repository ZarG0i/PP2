import pygame
import sys

from Racer import RacerGame
from ui import draw_button, draw_center_text
from persistence import load_settings

pygame.init()

WIDTH=400
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TSIS 3 Racer")

clock=pygame.time.Clock()

settings=load_settings()

state="menu"

game = RacerGame(screen, settings)


def menu_loop():
    global state

    screen.fill((230,230,230))

    draw_center_text(screen,"RACER GAME",80,40)

    play_rect = draw_button(screen,"Play",140,180,120,45)
    leader_rect= draw_button(screen,"Leaderboard",120,250,160,45)
    settings_rect=draw_button(screen,"Settings",130,320,140,45)
    quit_rect=draw_button(screen,"Quit",145,390,110,45)

    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()[0]

    if click:
        if play_rect.collidepoint(mouse):
            state="game"

        elif leader_rect.collidepoint(mouse):
            state="leaderboard"

        elif settings_rect.collidepoint(mouse):
            state="settings"

        elif quit_rect.collidepoint(mouse):
            pygame.quit()
            sys.exit()


while True:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state=="game":
            game.handle_event(event)

    if state=="menu":
        menu_loop()

    elif state=="game":
        result=game.update_draw()

        if result=="gameover":
            state="gameover"

    elif state=="gameover":

        screen.fill((255,255,255))
        draw_center_text(screen,"GAME OVER",200,50)
        draw_center_text(screen,f"Score {game.score}",260,35)

        retry=draw_button(screen,"Retry",145,340,110,45)
        menu=draw_button(screen,"Menu",145,400,110,45)

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()[0]

        if click:
            if retry.collidepoint(mouse):
                game.reset()
                state="game"

            if menu.collidepoint(mouse):
                game.reset()
                state="menu"

    elif state=="leaderboard":
        from persistence import get_scores

        screen.fill((255,255,255))

        draw_center_text(screen,"TOP 10",60,40)

        scores=get_scores()

        y=120
        for i,s in enumerate(scores):
            draw_center_text(
                screen,
                f"{i+1}. {s['name']} {s['score']}",
                y,
                28
            )
            y+=35

        back=draw_button(screen,"Back",145,520,110,40)

        if pygame.mouse.get_pressed()[0]:
            if back.collidepoint(pygame.mouse.get_pos()):
                state="menu"

    elif state=="settings":

        screen.fill((245,245,245))
        draw_center_text(screen,"SETTINGS",100,40)

        draw_center_text(
            screen,
            f"Difficulty: {settings['difficulty']}",
            220,
            30
        )

        easy=draw_button(screen,"Easy",60,320,90,40)
        med=draw_button(screen,"Medium",155,320,90,40)
        hard=draw_button(screen,"Hard",250,320,90,40)

        back=draw_button(screen,"Back",145,430,110,40)

        if pygame.mouse.get_pressed()[0]:
            m=pygame.mouse.get_pos()

            if easy.collidepoint(m):
                settings["difficulty"]="easy"

            if med.collidepoint(m):
                settings["difficulty"]="medium"

            if hard.collidepoint(m):
                settings["difficulty"]="hard"

            if back.collidepoint(m):
                state="menu"

    pygame.display.update()
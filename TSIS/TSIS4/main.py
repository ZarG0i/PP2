import pygame
from game import run_game
import db

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake TSIS4")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
WHITE_PURPLE = (230, 230, 250) 

font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()


# ---------------- BUTTON ----------------
def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)

    color = GRAY if not rect.collidepoint(pygame.mouse.get_pos()) else (170,170,170)

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    label = small_font.render(text, True, BLACK)
    screen.blit(label, (x + 20, y + 10))

    return rect


# ---------------- USERNAME ----------------
def get_username():
    name = ""

    while True:
        screen.fill(WHITE)

        screen.blit(small_font.render("Enter your name:", True, BLACK), (200, 150))
        screen.blit(font.render(name, True, BLACK), (200, 200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name if name else "Player"
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        clock.tick(60)


# ---------------- LEADERBOARD ----------------
def leaderboard_screen():
    data = db.get_leaderboard()

    while True:
        screen.fill(WHITE)

        screen.blit(font.render("LEADERBOARD", True, BLACK), (150, 50))

        y = 120
        for i, row in enumerate(data):
            text = f"{i+1}. {row[0]} | {row[1]} | lvl {row[2]}"
            screen.blit(small_font.render(text, True, BLACK), (100, y))
            y += 35

        back_btn = draw_button("Back", 220, 420, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "menu"

        clock.tick(60)


# ---------------- MENU ----------------
def main_menu():
    while True:
        screen.fill(WHITE)

        screen.blit(font.render("SNAKE GAME", True, BLACK), (190, 80))

        play_btn = draw_button("Play", 220, 200, 160, 50)
        board_btn = draw_button("Leaderboard", 220, 270, 160, 50)
        quit_btn = draw_button("Quit", 220, 340, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    return "play"
                if board_btn.collidepoint(event.pos):
                    return "leaderboard"
                if quit_btn.collidepoint(event.pos):
                    return "quit"

        clock.tick(60)


# ---------------- GAME OVER ----------------
def game_over_screen(score, level):
    while True:
        screen.fill(WHITE)

        screen.blit(font.render("GAME OVER", True, BLACK), (160, 120))
        screen.blit(small_font.render(f"Score: {score}", True, WHITE), (220, 200))
        screen.blit(small_font.render(f"Level: {level}", True, WHITE), (220, 240))

        retry_btn = draw_button("Retry", 220, 300, 160, 50)
        menu_btn = draw_button("Menu", 220, 360, 160, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(event.pos):
                    return "retry"
                if menu_btn.collidepoint(event.pos):
                    return "menu"

        clock.tick(60)


# ---------------- MAIN LOOP ----------------
def main():
    db.create_tables()

    state = "menu"

    while True:

        if state == "menu":
            result = main_menu()

            if result == "play":
                state = "play"
            elif result == "leaderboard":
                state = "leaderboard"
            elif result == "quit":
                break

        elif state == "leaderboard":
            result = leaderboard_screen()

            if result == "menu":
                state = "menu"
            elif result == "quit":
                break

        elif state == "play":
            username = get_username()
            if username is None:
                break

            result = run_game(screen, username, db)

            if result == "quit":
                break

            elif result[0] == "game_over":
                score, level = result[1], result[2]
                state = "game_over"

        elif state == "game_over":
            result = game_over_screen(score, level)

            if result == "retry":
                state = "play"
            elif result == "menu":
                state = "menu"
            elif result == "quit":
                break

    pygame.quit()


if __name__ == "__main__":
    main()
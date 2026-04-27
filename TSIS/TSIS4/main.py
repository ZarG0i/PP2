import pygame
import json
import os
from game import Game
from db import Database
from config import WIDTH, HEIGHT, FPS, SETTINGS_FILE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Advanced")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def load_settings():
    defaults = {"snake_color": [0, 255, 0], "grid": False, "sound": True}
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                loaded = json.load(f)
                defaults.update(loaded)
        except:
            pass
    return defaults

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=2)

class MainMenu:
    def __init__(self):
        self.buttons = [
            ("Play", 250, 200),
            ("Leaderboard", 250, 280), 
            ("Settings", 250, 360),
            ("Quit", 250, 440)
        ]
        self.selected = 0
        
    def handle_event(self, event, db, settings):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.buttons)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.buttons)
            elif event.key == pygame.K_RETURN:
                return self.buttons[self.selected][0]
        return None
    
    def draw(self, screen, username, personal_best):
        screen.fill((20, 20, 40))
        
        title = font.render("SNAKE GAME", True, (0, 255, 0))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        if username:
            pb_text = font.render(f"Personal Best: {personal_best}", True, (255, 255, 255))
            screen.blit(pb_text, (WIDTH//2 - pb_text.get_width()//2, 150))
        
        for i, (text, x, y) in enumerate(self.buttons):
            color = (0, 255, 0) if i == self.selected else (100, 255, 100)
            surf = font.render(text, True, color)
            screen.blit(surf, (x, y))

def main():
    db = Database()
    settings = load_settings()
    username = input("Enter username: ")  # Simple console input
    
    db.create_player(username)
    personal_best = db.get_personal_best(username)
    
    main_menu = MainMenu()
    game = None
    current_screen = "menu"
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if current_screen == "menu":
                result = main_menu.handle_event(event, db, settings)
                if result == "Play":
                    game = Game(db, settings, username)
                    current_screen = "game"
                elif result == "Quit":
                    running = False
            
            elif current_screen == "game" and game:
                action = game.handle_event(event)
                if action == "menu":
                    current_screen = "menu"
        
        screen.fill((0, 0, 0))
        
        if current_screen == "menu":
            main_menu.draw(screen, username, personal_best)
        elif current_screen == "game" and game:
            game.update()
            game.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
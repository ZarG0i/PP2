import pygame
import random
import json
from config import *

class Game:
    def __init__(self, db, settings, username):
        self.db = db
        self.settings = settings
        self.username = username
        self.reset_game()
        self.state = "playing"
        
    def reset_game(self):
        self.snake = [(300, 300), (280, 300), (260, 300)]
        self.direction = (CELL, 0)
        self.score = 0
        self.level = 1
        self.speed = 8
        self.foods = [self.spawn_food() for _ in range(MAX_FOODS)]
        self.powerup = None
        self.obstacles = []
        self.shield_active = False
        self.speed_boost_end = 0
        self.slow_motion_end = 0
        self.font = pygame.font.SysFont(None, 24)
        self.small_font = pygame.font.SysFont(None, 20)
        
    def spawn_food(self):
        while True:
            x = random.randrange(0, WIDTH, CELL)
            y = random.randrange(0, HEIGHT, CELL)
            pos = (x, y)
            if (pos not in [s for s in self.snake] and 
                pos not in self.obstacles):
                weight = random.choice([1, 2, 3])
                is_poison = random.random() < 0.2
                return {
                    "pos": pos,
                    "weight": -2 if is_poison else weight,
                    "spawn_time": pygame.time.get_ticks(),
                    "is_poison": is_poison
                }
    
    def spawn_powerup(self):
        if random.random() < 0.005:  # Rare spawn
            while True:
                x = random.randrange(0, WIDTH, CELL)
                y = random.randrange(0, HEIGHT, CELL)
                pos = (x, y)
                if (pos not in [s for s in self.snake] and 
                    pos not in self.obstacles and 
                    pos not in [f["pos"] for f in self.foods]):
                    types = ["speed", "slow", "shield"]
                    self.powerup = {
                        "pos": pos,
                        "type": random.choice(types),
                        "spawn_time": pygame.time.get_ticks()
                    }
                    break
    
    def generate_obstacles(self):
        self.obstacles = []
        num_obstacles = max(0, self.level - 2)
        for _ in range(num_obstacles):
            while True:
                x = random.randrange(0, WIDTH, CELL)
                y = random.randrange(0, HEIGHT, CELL)
                pos = (x, y)
                if (pos not in [s for s in self.snake] and 
                    pos not in [f["pos"] for f in self.foods]):
                    self.obstacles.append(pos)
                    break
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return "quit"
            
        if self.state == "playing" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.direction != (0, CELL):
                self.direction = (0, -CELL)
            elif event.key == pygame.K_s and self.direction != (0, -CELL):
                self.direction = (0, CELL)
            elif event.key == pygame.K_a and self.direction != (CELL, 0):
                self.direction = (-CELL, 0)
            elif event.key == pygame.K_d and self.direction != (-CELL, 0):
                self.direction = (CELL, 0)
            elif event.key == pygame.K_ESCAPE:
                return "menu"
        
        return None
    
    def update(self):
        if self.state != "playing":
            return
            
        current_time = pygame.time.get_ticks()
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        
        # Boundary collision
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT):
            if self.shield_active:
                self.shield_active = False
            else:
                self.game_over()
                return
        
        # Self collision
        if head in self.snake:
            if self.shield_active:
                self.shield_active = False
            else:
                self.game_over()
                return
        
        # Obstacle collision
        if head in self.obstacles:
            self.game_over()
            return
        
        self.snake.insert(0, head)
        
        # Food collision
        eaten = False
        for i, food in enumerate(self.foods[:]):
            if head == food["pos"]:
                weight = food["weight"]
                if weight > 0:
                    self.score += weight
                else:  # poison
                    for _ in range(2):
                        if len(self.snake) > 1:
                            self.snake.pop()
                    if len(self.snake) <= 1:
                        self.game_over()
                        return
                self.foods[i] = self.spawn_food()
                eaten = True
                break
        
        # Powerup collision
        if self.powerup and head == self.powerup["pos"]:
            ptype = self.powerup["type"]
            if ptype == "speed":
                self.speed_boost_end = current_time + 5000
            elif ptype == "slow":
                self.slow_motion_end = current_time + 5000
            elif ptype == "shield":
                self.shield_active = True
            self.powerup = None
        
        if not eaten:
            self.snake.pop()
        
        # Cleanup expired food/powerups
        self.foods = [f for f in self.foods if current_time - f["spawn_time"] < FOOD_LIFETIME]
        while len(self.foods) < MAX_FOODS:
            self.foods.append(self.spawn_food())
        
        if self.powerup and current_time - self.powerup["spawn_time"] > 8000:
            self.powerup = None
        
        self.spawn_powerup()
        
        # Level up
        new_level = self.score // 3 + 1
        if new_level > self.level:
            self.level = new_level
            self.speed += 1
            if self.level >= 3:
                self.generate_obstacles()
    
    def game_over(self):
        self.state = "game_over"
        self.db.save_session(self.username, self.score, self.level)
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Grid
        if self.settings.get("grid", False):
            for x in range(0, WIDTH, CELL):
                pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, CELL):
                pygame.draw.line(screen, (20, 20, 20), (0, y), (WIDTH, y))
        
        # Snake
        snake_color = self.settings.get("snake_color", [0, 255, 0])
        for segment in self.snake:
            pygame.draw.rect(screen, snake_color, (*segment, CELL, CELL))
        
        if self.shield_active:
            pygame.draw.rect(screen, (255, 255, 0), (*self.snake[0], CELL, CELL), 3)
        
        # Foods
        for food in self.foods:
            color = (139, 0, 0) if food["is_poison"] else (
                (255, 0, 0) if food["weight"] == 1 else 
                (0, 120, 255) if food["weight"] == 2 else (255, 255, 255)
            )
            pygame.draw.rect(screen, color, (*food["pos"], CELL, CELL))
            text = self.small_font.render(str(abs(food["weight"])), True, (0, 0, 0))
            screen.blit(text, (food["pos"][0] + 4, food["pos"][1] + 2))
        
        # Powerup
        if self.powerup:
            colors = {"speed": (255, 255, 0), "slow": (128, 128, 255), "shield": (255, 0, 255)}
            color = colors.get(self.powerup["type"], (255, 255, 255))
            pygame.draw.rect(screen, color, (*self.powerup["pos"], CELL, CELL))
        
        # Obstacles
        for obs in self.obstacles:
            pygame.draw.rect(screen, (100, 100, 100), (*obs, CELL, CELL))
        
        # UI
        ui_text = self.font.render(f"Score: {self.score}  Level: {self.level}  Speed: {self.speed}", True, (255, 255, 255))
        screen.blit(ui_text, (10, 10))
        
        if self.state == "game_over":
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))
            
            go_text = self.font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(go_text, (WIDTH//2 - 80, HEIGHT//2 - 50))
            
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            screen.blit(score_text, (WIDTH//2 - 70, HEIGHT//2))
            
            info_text = self.small_font.render("ESC - Menu  R - Restart", True, (200, 200, 200))
            screen.blit(info_text, (WIDTH//2 - 100, HEIGHT//2 + 40))
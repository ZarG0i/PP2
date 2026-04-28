import pygame
import random
import json
import os

# ---------- SETTINGS ----------
CELL_SIZE = 25
COLUMNS = 24
ROWS = 20

WIDTH = COLUMNS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE


BROWN = (139, 69, 19)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (220,50,50)
DARK_RED = (120,0,0)

YELLOW = (255,200,0)
BLUE = (50,100,255)
CYAN = (0,200,200)
OBSTACLE_COLOR = (100,100,100)

FPS_START = 6

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

default_settings = {
    "snake_color": [0, 170, 0],
    "grid": True,
    "sound": False
}

try:
    with open(SETTINGS_PATH, "r") as f:
        settings = json.load(f)
except:
    settings = default_settings

snake_color_list = settings.get("snake_color", [0,170,0])
SNAKE_COLOR = tuple(snake_color_list)
GRID_ON = settings.get("grid", True)

# ---------- UTILS ----------
def get_random_position(snake, obstacles=set()):
    while True:
        pos = (random.randint(1, COLUMNS-2), random.randint(1, ROWS-2))
        if pos not in snake and pos not in obstacles:
            return pos

def draw_cell(screen, pos, color):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def draw_grid(screen):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (200,200,200), (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (200,200,200), (0,y), (WIDTH,y))

def generate_obstacles(snake, count=10):
    obstacles = set()
    while len(obstacles) < count:
        pos = (random.randint(2, COLUMNS-3), random.randint(2, ROWS-3))
        if pos not in snake:
            obstacles.add(pos)
    return obstacles

# ---------- GAME ----------
def run_game(screen, username, db):

    clock = pygame.time.Clock()

    snake = [(10,10), (9,10), (8,10)]
    direction = (1,0)

    obstacles = set()

    food = get_random_position(snake, obstacles)

    # 🟥 POISON FOOD
    poison = get_random_position(snake, obstacles)

    # ⚡ POWER UPS
    power = None
    power_type = None
    power_spawn_time = 0

    active_power = None
    power_end_time = 0

    shield_active = False

    score = 0
    level = 1
    speed = FPS_START

    font = pygame.font.SysFont("Arial", 20)

    while True:

        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0,1):
                    direction = (0,-1)
                elif event.key == pygame.K_DOWN and direction != (0,-1):
                    direction = (0,1)
                elif event.key == pygame.K_LEFT and direction != (1,0):
                    direction = (-1,0)
                elif event.key == pygame.K_RIGHT and direction != (-1,0):
                    direction = (1,0)

        # ---------- POWER SPAWN ----------
        if power is None and random.random() < 0.01:
            power = get_random_position(snake, obstacles)
            power_type = random.choice(["speed", "slow", "shield"])
            power_spawn_time = now

        if power and now - power_spawn_time > 8000:
            power = None

        # ---------- POWER EFFECT ----------
        current_speed = speed
        if active_power == "speed":
            current_speed += 3
        elif active_power == "slow":
            current_speed = max(3, speed - 3)

        # ---------- MOVE ----------
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # ---------- COLLISION ----------
        if (
            not (0 < head[0] < COLUMNS-1 and 0 < head[1] < ROWS-1)
            or head in snake
            or head in obstacles
        ):
            if shield_active:
                shield_active = False
            else:
                db.save_game(username, score, level)
                return ("game_over", score, level)

        snake.insert(0, head)

        # ---------- FOOD ----------
        if head == food:
            score += 1
            if score % 4 == 0:
                level += 1
                speed += 1

                if level >= 3:
                    obstacles = generate_obstacles(snake)

            food = get_random_position(snake, obstacles)

        # ---------- 🟥 POISON FOOD ----------
        elif head == poison:
            snake.pop()
            snake.pop()

            if len(snake) <= 1:
                db.save_game(username, score, level)
                return ("game_over", score, level)

            poison = get_random_position(snake, obstacles)

        # ---------- ⚡ POWER PICKUP ----------
        elif power and head == power:

            if power_type == "speed":
                active_power = "speed"
                power_end_time = now + 5000

            elif power_type == "slow":
                active_power = "slow"
                power_end_time = now + 5000

            elif power_type == "shield":
                shield_active = True

            power = None

        else:
            snake.pop()

        # ---------- POWER TIMER ----------
        if active_power and now > power_end_time:
            active_power = None

        # ---------- DRAW ----------
        screen.fill(BLACK)

        if GRID_ON:
            draw_grid(screen)

        # obstacles
        for obs in obstacles:
            draw_cell(screen, obs, OBSTACLE_COLOR)

        # snake
        for s in snake:
            draw_cell(screen, s, SNAKE_COLOR)

        # food
        draw_cell(screen, food, RED)

        # poison
        draw_cell(screen, poison, GREEN)

        # power
        if power:
            colors = {
                "speed": BLUE,
                "slow": BROWN,
                "shield": CYAN
            }
            draw_cell(screen, power, colors[power_type])

        # shield effect
        if shield_active:
            pygame.draw.circle(
                screen,
                CYAN,
                (snake[0][0]*CELL_SIZE + CELL_SIZE//2,
                 snake[0][1]*CELL_SIZE + CELL_SIZE//2),
                CELL_SIZE,
                2
            )

        screen.blit(font.render(f"Score: {score}", True, WHITE), (5,5))
        screen.blit(font.render(f"Level: {level}", True, WHITE), (5,25))

        pygame.display.flip()
        clock.tick(current_speed)
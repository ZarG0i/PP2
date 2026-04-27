import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,120,255)
BLACK = (0,0,0)

snake = [(300,300), (280,300), (260,300)]
direction = (CELL, 0)

score = 0
level = 1
speed = 8

font = pygame.font.SysFont(None, 30)

FOOD_LIFETIME = 5000  # ms = 5 seconds
MAX_FOODS = 3


def spawn_food():
    """Spawn food with random weight"""
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            weight = random.choice([1, 2, 3])  # different values
            return {
                "pos": (x, y),
                "weight": weight,
                "spawn_time": pygame.time.get_ticks()
            }


foods = [spawn_food() for _ in range(MAX_FOODS)]

running = True
while running:
    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = (0, -CELL)
            elif event.key == pygame.K_s:
                direction = (0, CELL)
            elif event.key == pygame.K_a:
                direction = (-CELL, 0)
            elif event.key == pygame.K_d:
                direction = (CELL, 0)

    # MOVE SNAKE
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        running = False

    if head in snake:
        running = False

    snake.insert(0, head)

    # FOOD LOGIC
    eaten_index = None

    for i, food in enumerate(foods):
        fx, fy = food["pos"]

        # check collision
        if head == (fx, fy):
            score += food["weight"]
            eaten_index = i

        # check expiration
        if current_time - food["spawn_time"] > FOOD_LIFETIME:
            foods[i] = spawn_food()

    if eaten_index is not None:
        foods[eaten_index] = spawn_food()
    else:
        snake.pop()

    # DRAW SNAKE
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # DRAW FOODS
    for food in foods:
        fx, fy = food["pos"]
        weight = food["weight"]

        # color depends on weight
        color = RED if weight == 1 else BLUE if weight == 2 else WHITE

        pygame.draw.rect(screen, color, (fx, fy, CELL, CELL))

        # show weight number
        w_text = font.render(str(weight), True, BLACK)
        screen.blit(w_text, (fx + 5, fy + 2))

    # UI
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    # level system
    if score // 3 + 1 != level:
        level = score // 3 + 1
        speed += 1

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
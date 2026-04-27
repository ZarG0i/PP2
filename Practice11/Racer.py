import pygame
import sys
import random

pygame.init()

# ---------------- SCREEN ----------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()
FPS = 60

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)

# ---------------- IMAGES ----------------
player_img = pygame.image.load("C:/Users/ZANGAR/Desktop/PP2/Practice10/images/Designer.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 80))

enemy_img = pygame.image.load("C:/Users/ZANGAR/Desktop/PP2/Practice10/images/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (50, 80))
enemy_img = pygame.transform.rotate(enemy_img, 180)

road_img = pygame.image.load("C:/Users/ZANGAR/Desktop/PP2/Practice10/images/roadPP.png").convert()
road_img = pygame.transform.scale(road_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# ---------------- PLAYER ----------------
player = player_img.get_rect()
player.x = 200
player.y = 500

# ---------------- ENEMY ----------------
enemy = enemy_img.get_rect()
enemy.x = random.randint(50, 160)
enemy.y = -100

# ---------------- COINS (WEIGHTED) ----------------
coins = []

for i in range(5):
    weight = random.randint(1, 3)

    if weight == 1:
        radius = 8
    elif weight == 2:
        radius = 12
    else:
        radius = 16

    coin = {
        "rect": pygame.Rect(
            random.randint(40, 350),
            random.randint(-600, 0),
            radius * 2,
            radius * 2
        ),
        "value": weight,
        "radius": radius
    }

    coins.append(coin)

# ---------------- ROAD ----------------
road_y1 = 0
road_y2 = -SCREEN_HEIGHT

# ---------------- GAME DATA ----------------
speed = 5
score = 0
font = pygame.font.SysFont("Bookman old style", 20)
game_over = False

# speed increase timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

# ---------------- TEXT ----------------
def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# ---------------- GAME LOOP ----------------
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:
            speed += 0.5

    if not game_over:

        # -------- ROAD --------
        road_y1 += speed
        road_y2 += speed

        if road_y1 >= SCREEN_HEIGHT:
            road_y1 = -SCREEN_HEIGHT
        if road_y2 >= SCREEN_HEIGHT:
            road_y2 = -SCREEN_HEIGHT

        # -------- INPUT --------
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.width:
            player.x += 5
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= 5
        if keys[pygame.K_DOWN] and player.y < SCREEN_HEIGHT - player.height:
            player.y += 5

        # -------- ENEMY --------
        enemy.y += speed

        if enemy.y > SCREEN_HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(40, 350)

        if player.colliderect(enemy):
            game_over = True

        # -------- COINS FIXED LOGIC --------
        for coin in coins:

            coin["rect"].y += speed

            # respawn
            if coin["rect"].y > SCREEN_HEIGHT:

                weight = random.randint(1, 3)

                if weight == 1:
                    radius = 8
                elif weight == 2:
                    radius = 12
                else:
                    radius = 16

                coin["value"] = weight
                coin["radius"] = radius
                coin["rect"] = pygame.Rect(
                    random.randint(40, 350),
                    random.randint(-600, 0),
                    radius * 2,
                    radius * 2
                )

            # collision
            if player.colliderect(coin["rect"]):
                score += coin["value"]

                weight = random.randint(1, 3)

                if weight == 1:
                    radius = 8
                elif weight == 2:
                    radius = 12
                else:
                    radius = 16

                coin["value"] = weight
                coin["radius"] = radius
                coin["rect"] = pygame.Rect(
                    random.randint(40, 350),
                    random.randint(-600, 0),
                    radius * 2,
                    radius * 2
                )

        # -------- DRAW ROAD --------
        screen.blit(road_img, (0, road_y1))
        screen.blit(road_img, (0, road_y2))

        # -------- DRAW OBJECTS --------
        screen.blit(player_img, player)
        screen.blit(enemy_img, enemy)

        # coins draw FIXED
        for coin in coins:

            if coin["value"] == 1:
                color = (255, 255, 0)   # gold
            elif coin["value"] == 2:
                color = (255, 165, 0) # silver
            else:
                color = (255, 140, 0)   # rare

            pygame.draw.circle(
                screen,
                color,
                coin["rect"].center,
                coin["radius"]
            )

        # -------- UI --------
        draw_text(f"Coins: {score}", 10, 10)
        draw_text(f"Speed: {speed:.1f}", 10, 35)

    else:
        draw_text("GAME OVER", 130, 250, RED)
        draw_text(f"Score: {score}", 150, 300, BLACK)

    pygame.display.update()
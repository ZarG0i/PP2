import pygame

class Ball:
    def __init__(self, x=300, y=200):
        self.x = x
        self.y = y
        self.radius = 25
        self.step = 20

        self.width = 800
        self.height = 600

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # boundary check
        if 0 + self.radius <= new_x <= self.width - self.radius:
            self.x = new_x
        if 0 + self.radius <= new_y <= self.height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
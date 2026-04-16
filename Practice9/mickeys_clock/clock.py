import pygame
import math
from datetime import datetime

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 300)

        self.hand_image = pygame.image.load("images/mickey_hand2.jpg")
        self.hand_image = pygame.transform.scale(self.hand_image, (150, 20))

    def get_time_angles(self):
        now = datetime.now()
        minutes = now.minute
        seconds = now.second

        # 360 degrees total
        minute_angle = -(minutes * 6)
        second_angle = -(seconds * 6)

        return minute_angle, second_angle

    def draw_hand(self, image, angle, offset):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=offset)
        self.screen.blit(rotated, rect)

    def update(self):
        self.screen.fill((255, 255, 255))

        minute_angle, second_angle = self.get_time_angles()

        # Right = minutes
        self.draw_hand(self.hand_image, minute_angle, self.center)

        # Left = seconds (slightly offset)
        self.draw_hand(self.hand_image, second_angle, (self.center[0]-30, self.center[1]))
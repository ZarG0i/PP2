import pygame
import math
from datetime import datetime

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 300)

        
        self.bg = pygame.image.load("C:/Users/ZANGAR/Desktop/Practice9/mickeys_clock/images/clock.jpg")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

    def get_time_angles(self):
        now = datetime.now()

        seconds = now.second + now.microsecond / 1_000_000
        minutes = now.minute + seconds / 60

        second_angle = seconds * 6
        minute_angle = minutes * 6

        return minute_angle, second_angle

    def draw_hand(self, angle_deg, length, color, width):
        angle_rad = math.radians(angle_deg - 90)

        x = self.center[0] + length * math.cos(angle_rad)
        y = self.center[1] + length * math.sin(angle_rad)

        pygame.draw.line(self.screen, color, self.center, (x, y), width)

    def update(self):
        self.screen.blit(self.bg, (0, 0))

        minute_angle, second_angle = self.get_time_angles()

        self.draw_hand(minute_angle, 150, (0, 0, 0), 10)   
        self.draw_hand(second_angle, 250, (1, 0, 0), 8)

       
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 6)
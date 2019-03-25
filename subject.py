from constants import *
import random
if DO_VISUALS:
    import pygame

class Subject:
    def __init__(self, w, h, minR, maxR):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.r = random.randint(minR, maxR)
        self.vx = random.randint(-w / 2, w / 2) 
        self.vy = random.randint(-h / 2, h / 2) 
        r = random.randint(100,255)
        g = random.randint(100,255)
        b = random.randint(100,255)
        self.color = [r, g, b]
        self.screenW = w
        self.screenH = h
        self.id = Subject.id
        Subject.id += 1

    def move(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt
        if self.x - self.r <= 0:
            self.vx *= -1
            self.x = self.r
        if self.x + self.r >= self.screenW:
            self.vx *= -1
            self.x = self.screenW - self.r
        if self.y - self.r <= 0:
            self.vy *= -1
            self.y = self.r
        if self.y + self.r >= self.screenH:
            self.vy *= -1
            self.y = self.screenH - self.r

    def render(self, surf):
        pygame.draw.circle(surf, self.color, [int(self.x), int(self.y)], self.r)    

from constants import *
import random
if DO_VISUALS:
    import pygame

class Trap:
    def __init__(self, w, h, r):
        self.x = random.randint(r, w - r)
        self.y = random.randint(r, h - r)
        self.r = r
        self.color = [50, 200, 100]
        self.edgeColor = [50, 100, 200]
        self.screenW = w
        self.screenH = h

    def render(self, surf):
        pygame.draw.circle(surf, self.edgeColor, [int(self.x), int(self.y)], self.r)    
        pygame.draw.circle(surf, self.color, [int(self.x), int(self.y)], self.r - 5)    

    def checkCollision(self, sub):
        distSquared = (self.x - sub.x) * (self.x - sub.x) + (self.y - sub.y) * (self.y - sub.y)
        radiiSquared = (self.r + sub.r) * (self.r + sub.r)
        if distSquared < radiiSquared:
            return True
        return False

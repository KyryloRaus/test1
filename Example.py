import pygame
from random import randint
import sys
pygame.init()

clock = pygame.time.Clock()
back = (255, 255, 255) #background
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)

BLACK = (0, 0, 0)
GREEN = (0,200,0)
RED = (180,0,0)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self,new_color):
        self.fill_color = new_color #зміна кольору картки
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, line_color, line_width):
        pygame.draw.rect(mw, line_color, self.rect, line_width)
    def cp(self, x, y):
        return self.rect.collidepoint(x, y)
class Label(Area):
    def set_text(self, text, fsize=12, text_color= BLACK):
        self.image = pygame.font.SysFont("times new roman", fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

points = 0
cards = []
numbers = 4
x = 36
YELLOW = (255, 234, 0)
BLUE = (2, 3, 226)
for i in range(numbers):
    card = Label(x, 200, 80, 120, YELLOW)
    card.outline(BLUE, 15)
    card.set_text("CLICK",20)
    cards.append(card)
    x=x+116

wait = 0
while True:
    if wait == 0:
        wait = 60
        click = randint(1, 4)
        for i in range(4):
            cards[i].color(YELLOW)
            if i+1 == click:
                cards[i].draw(15,40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
            
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos
            for i in range(4):
                if cards[i].cp(x,y):
                    if i+1 == click:
                        cards[i].color(GREEN)
                        points=points+1
                    else:
                        cards[i].color(RED)
                        points=points-1
                    cards[i].fill()
    clock.tick(40)
    pygame.display.update()
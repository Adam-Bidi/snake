from random import randint
import pygame as pg
pg.init()
screen = pg.display.set_mode((400,300))
clock = pg.time.Clock()
while True : 
    clock.tick(1)
    for event in pg.event.get():
        pass
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    screen.fill(random_color)
    pg.display.update()
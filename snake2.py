"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg
from collections import deque

height = 40
width = 40
size = 20

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

score = 0
pg.display.set_caption(f"Score: {score}")

borders = []
for k in range(0,600):
    borders.append((k,-1))
    borders.append((-1,k))
    borders.append((601,k))
    borders.append((k,601))

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
screen.fill(white)
# conditions initiales
snake = deque([(15,5),(16,5),(17,5)])
direction = (-1,0)
fruit_x, fruit_y = randint(0,20), randint(0,20)

def handle_event(event):
    global direction
    # chaque évênement à un type qui décrit la nature de l'évênement
    # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
    if event.type == pg.QUIT:
        running = False
    # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
    elif event.type == pg.KEYDOWN:
        # si la touche est "Q" on veut quitter le programme
        if event.key == pg.K_q:
            running = False
        if event.key == pg.K_UP:
            if direction != (0,1):
                direction = (0,-1)
        if event.key == pg.K_DOWN:
            if direction != (0,-1):
                direction = (0,1)
        if event.key == pg.K_LEFT:
            if direction != (1,0):
                direction = (-1,0)
        if event.key == pg.K_RIGHT:
            if direction != (-1,0):
                direction = (1,0)

while running:
    clock.tick(10)
    screen.fill(white)

    for x in range(width): # coloriage du damier
        for y in range(height):
            rect = pg.Rect(x * size, y * size, size, size)
            color = white if (x+y)%2 == 0 else black
            pg.draw.rect(screen, color, rect)

    first_x, first_y = snake[0]
    direction_x, direction_y = direction
    snake.pop()
    if (first_x + direction_x, first_y + direction_y) in snake:
        running = False
    if (first_x + direction_x, first_y + direction_y) in borders:
        running = False
    else :
        snake.appendleft((first_x + direction_x, first_y + direction_y))
    
   
    fruit = (fruit_x, fruit_y)
    pg.draw.rect(screen, green, pg.Rect(fruit_x * size, fruit_y * size, size, size))


    for (x,y) in snake : 
        rect = pg.Rect(x * size, y * size, size, size)

        pg.draw.rect(screen, red, rect)

    if snake[0] == fruit:
        snake.appendleft(fruit)
        score += 1
        pg.display.set_caption(f"Score: {score}")
        fruit_x, fruit_y = randint(0,20), randint(0,20)
        
 
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        handle_event(event)
            


    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

    pg.display.update()
    

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()




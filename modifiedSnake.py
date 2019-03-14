
import pygame
import random

pygame.init()
win_height = 501
win_width = 501
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")

x = 50
y = 50
width = 19
height = 19
vel = 1
lineColor = (0,0,255)
snakeColor = (255,0,0)

L = False
R = True
U = False
D = False

curr = [(41,41),(21,41),(1,41)]

run = True
for i in curr:
    pygame.draw.rect(win, snakeColor, (i[0], i[1], width, height))

for i in range(0,501,20):
    pygame.draw.line(win, lineColor, (i,0), (i,500))
for i in range(0,501,20):
    pygame.draw.line(win, lineColor, (0,i), (500,i))
randomx = random.randrange(1, 482, 20)
randomy = random.randrange(1, 482, 20)
pygame.draw.rect(win, snakeColor, (randomx, randomy, width, height))
pygame.display.update()

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False






    # nwHead = (curr[0][0]+width+1,curr[0][1])
    # curr.insert(0,nwHead)
    curr.pop()

    # UPDATE HEAD
    if L:
        tmp = curr[0][0]-width-1
        if tmp < 0:
            tmp = win_width-width-1
        nwHead = (tmp,curr[0][1])
        curr.insert(0,nwHead)
    if R:
        nwHead = ((curr[0][0]+width+1)%(win_width-1),curr[0][1])
        curr.insert(0,nwHead)
    if U:
        tmp = curr[0][1]-height-1
        if tmp < 0:
            tmp = win_height-height-1
        nwHead = (curr[0][0],tmp)
        curr.insert(0,nwHead)
    if D:
        nwHead = (curr[0][0],(curr[0][1]+height+1)%(win_height-1))
        curr.insert(0,nwHead)

    # CHECK FOR OVERLAP
    for i in range(1,len(curr)):
        if curr[0][0] == curr[i][0] and curr[0][1] == curr[i][1]:
            curr = [(41,41),(21,41),(1,41)]
            break;

    # KEY CHECK
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        L = False
        R = True
        U = False
        D = False
    if keys[pygame.K_LEFT]:
        L = True
        R = False
        U = False
        D = False
    if keys[pygame.K_UP]:
        L = False
        R = False
        U = True
        D = False
    if keys[pygame.K_DOWN]:
        L = False
        R = False
        U = False
        D = True
    if curr[0][0] == randomx and curr[0][1] == randomy:
        if L:
            tmp = curr[0][0]-width-1
            if tmp < -width:
                tmp = win_width-1
            nwHead = (tmp,curr[0][1])
            curr.insert(0,nwHead)
        if R:
            nwHead = ((curr[0][0]+width+1)%win_width,curr[0][1])
            curr.insert(0,nwHead)
        if U:
            tmp = curr[0][1]-height-1
            if tmp < -height:
                tmp = win_height-1
            nwHead = (curr[0][0],tmp)
            curr.insert(0,nwHead)
        if D:
            nwHead = (curr[0][0],(curr[0][1]+height+1)%win_height)
            curr.insert(0,nwHead)
        randomx = random.randrange(1, 482, 20)
        randomy = random.randrange(1, 482, 20)
        
        # pygame.display.update()

    win.fill((0,0,0))
    for i in range(0,501,20):
        pygame.draw.line(win, lineColor, (i,0), (i,500))
    for i in range(0,501,20):
        pygame.draw.line(win, lineColor, (0,i), (500,i))
    for i in curr:
        pygame.draw.rect(win, snakeColor, (i[0], i[1], width, height))
    pygame.draw.rect(win, snakeColor, (randomx, randomy, width, height))
    pygame.display.update()

pygame.quit()
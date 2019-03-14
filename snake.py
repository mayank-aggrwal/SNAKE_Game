
import pygame
import random

pygame.init()
win_height = 500
win_width = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")

x = 50
y = 50
boxwidth = 20
width = 20
height = 20
vel = 1

L = False
R = True
U = False
D = False

curr = [(120,50),(99,50),(78,50),(57,50),(36,50)]

run = True
for i in curr:
    pygame.draw.rect(win, (0, 255,0), (i[0], i[1], width, height))


randomx = int(random.random()*(win_width-width))
randomy = int(random.random()*(win_height-height))
pygame.draw.rect(win, (0, 255,0), (randomx, randomy, width, height))
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
    if curr[0][0] > randomx-int(3*width/4) and curr[0][0] < randomx+int(7*width/4) and curr[0][1] > randomy-int(3*height/4) and curr[0][1] < randomy+int(7*height/4):
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
        randomx = int(random.random()*(win_width-width))
        randomy = int(random.random()*(win_height-height))
        
        # pygame.display.update()

    win.fill((0,0,0))
    for i in curr:
        pygame.draw.rect(win, (0, 255,0), (i[0], i[1], width, height))
    pygame.draw.rect(win, (0, 255,0), (randomx, randomy, width, height))
    pygame.display.update()

pygame.quit()
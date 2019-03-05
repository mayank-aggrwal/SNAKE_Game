
import pygame

pygame.init()
win_height = 500
win_width = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Rectangle Motion")

x = 50
y = 50
width = 30
height = 50
vel = 5
isJump = False
countJump = 10

run = True
while run:
    # print("Im here 1")
    pygame.time.delay(50)
    # print("Im here 2")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # print("Im here 3")
    keys = pygame.key.get_pressed()
    # print("Im here 4")
    if keys[pygame.K_RIGHT] and x <= win_width-width-vel:
        x += vel
    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
    if not(isJump):
        if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y <= win_height-height-vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    if isJump:
        if countJump >= -10:
            neg = 1
            if countJump < 0:
                neg = -1
            y -= (countJump ** 2) * neg * 0.5
            countJump -= 1
        else:
            isJump = False
            countJump = 10
    win.fill((0,0,0))
    # print("Im here 5")
    # pygame.display.update()
    # pygame.time.delay(1000)
    # print("Im here 6")
    pygame.draw.rect(win, (0, 255,0), (x, y, width, height))
    pygame.display.update()
    # print("Im here 7")

pygame.quit()
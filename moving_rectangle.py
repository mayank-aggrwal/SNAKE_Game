
import pygame

pygame.init()
win_height = 500
win_width = 500
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Rectangle Motion")

x = 50
y = 50
width = 30
height = 50
vel = 20

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
    if keys[pygame.K_RIGHT]:
        x += vel
        if x > win_width:
            x = -width
    if keys[pygame.K_LEFT]:
        x -= vel
        if x < -width:
            x = win_width
    if keys[pygame.K_UP]:
        y -= vel
        if y < -height:
            y = win_height
    if keys[pygame.K_DOWN]:
        y += vel
        if y > win_height:
            y = -height
    win.fill((0,0,0))
    # print("Im here 5")
    pygame.display.update()
    # pygame.time.delay(1000)
    # print("Im here 6")
    pygame.draw.rect(win, (0, 255,0), (x, y, width, height))
    pygame.display.update()
    # print("Im here 7")

pygame.quit()
import pygame,sys
from time import sleep
at_above=True

pygame.init()
screen = pygame.display.set_mode((680, 540))
screen.fill('white')
pygame.display.set_caption('test1')
image_A=pygame.image.load('A.png')
image_B=pygame.image.load('B.png')
image_A.set_colorkey('red')
image_B.set_colorkey('red')
A=image_A.get_rect()
B=image_B.get_rect()
screen.blit(image_A,A)
screen.blit(image_B,B)
A.center=((340,270))
B.center=((340,220))

def move_b():
    global B
    global at_above
    global screen
    for _ in range(50):
        if at_above:
            B=B.move(0,1)
        else:
            B=B.move(0,-1)
        screen.fill('white')
        screen.blit(image_A, A)
        screen.blit(image_B, B)
        pygame.display.update()
        sleep(0.01)
    if at_above:
        at_above=False
    else:
        at_above=True
    return 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            move_b()
        screen.fill('white')
        screen.blit(image_A, A)
        screen.blit(image_B, B)
        pygame.display.update()
        sleep(0.01)

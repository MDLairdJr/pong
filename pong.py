import pygame, sys
from pygame.locals import *

pygame.init()

background_image_filename = 'background.jpg'
paddle_size = (7, 30)

r_paddle_x = 700
r_paddle_y = 240-(paddle_size[1]/2)
r_move = 0
l_paddle_x = 100
l_paddle_y = 240-(paddle_size[1]/2)
l_move = 0

screen = pygame.display.set_mode((800,480),0, 32)
pygame.display.set_caption("Pong!")

background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                r_move -= 1
            elif event.key == K_DOWN:
                r_move += 1
            if event.key == K_w:
                l_move -= 1
            elif event.key == K_s:
                l_move += 1 
        elif event.type == KEYUP:
            if event.key == K_UP:
                r_move = 0
            if event.key == K_DOWN:
                r_move = 0
            if event.key == K_w:
                l_move = 0
            if event.key == K_s:
                l_move = 0
            
    screen.blit(background, (0,0))
        
    # First attempt at adding a paddle
    r_paddle_y += r_move
    l_paddle_y += l_move
    r_paddle_pos = (r_paddle_x, r_paddle_y)
    l_paddle_pos = (l_paddle_x, l_paddle_y)
    pygame.draw.rect(screen, (255,255,255), Rect(r_paddle_pos, paddle_size))
    pygame.draw.rect(screen, (255,255,255), Rect(l_paddle_pos, paddle_size))
        
    pygame.display.update()
    
    
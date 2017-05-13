#!C:\Python27\python.exe

import pygame, sys
from pygame.locals import *
import random
import math
import euclid  # from https://pypi.python.org/pypi/euclid

pygame.init()

background_image_filename = 'background.jpg'
SCREEN_SIZE = (800, 480)
paddle_size = (7, 30)
ball_size = (7, 7)
ball_pos = (397, 237)

r_paddle_x = 700
r_paddle_y = 240-(paddle_size[1]/2)
r_move = 0
l_paddle_x = 100
l_paddle_y = 240-(paddle_size[1]/2)
l_move = 0

# define variables for fps
fps_limit = 600

# define the initial velocity
initial_velocity = 80

# get the clock object
clock = pygame.time.Clock()

# set up the screen Surface
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Pong!")

background = pygame.image.load(background_image_filename).convert()

class Ball:
    def __init__(self, position, size, color = (0, 0, 0), velocity = euclid.Vector2(0,0), width = 0):
        # use a position vector instead of x and y coordinates
        self.position = position
        self.size = size 
        self.color = color 
        self.width = width
        self.velocity = velocity
        
    def draw(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.rect(screen, self.color, Rect((rx, ry), self.size))
        
    def move(self):
        self.position += self.velocity * dtime_s  
        self.bounce()
        
    def bounce(self):    
        if self.position.y <= 0:
            self.velocity = self.velocity.reflect(euclid.Vector2(0,1))
            
        elif self.position.y >= SCREEN_SIZE[1] - self.size[1]:
            self.velocity = self.velocity.reflect(euclid.Vector2(0,1))        
    
    
#######################################################
# this is just temporary
def get_random_velocity():
    new_angle = random.uniform(math.pi*0.25, math.pi*0.75)
    new_x = math.sin(new_angle)
    new_y = math.cos(new_angle)
    new_vector = euclid.Vector2(new_x, new_y)
    new_vector.normalize()
    new_vector *= initial_velocity   # pixels per second
    return new_vector
########################################################     
     
ball = Ball(euclid.Vector2(ball_pos[0], ball_pos[1]), ball_size, (255, 255, 255), get_random_velocity())
     
while True:
    # limit the frame rate and capture the time in 
    # milliseconds since the last tick (dtime_ms)
    dtime_ms = clock.tick(fps_limit)
    dtime_s = dtime_ms/1000.0         # time in seconds since the last tick

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
            
    # draw the background
    screen.blit(background, (0,0))
    
    # lock the screen
    screen.lock() 
        
    # adjust y-coordinate to account for paddle movement
    r_paddle_y += r_move
    l_paddle_y += l_move
    
    # make sure we don't go off the screen
    if r_paddle_y < 0:
        r_paddle_y = 0
    if r_paddle_y + paddle_size[1] > SCREEN_SIZE[1]: 
        r_paddle_y = SCREEN_SIZE[1] - paddle_size[1]
    if l_paddle_y < 0:
        l_paddle_y = 0
    if l_paddle_y + paddle_size[1] > SCREEN_SIZE[1]: 
        l_paddle_y = SCREEN_SIZE[1] - paddle_size[1]
        
    # create the tuple for the updated paddle position
    r_paddle_pos = (r_paddle_x, r_paddle_y)
    l_paddle_pos = (l_paddle_x, l_paddle_y)
    
    # draw the paddle rectangles
    pygame.draw.rect(screen, (255,255,255), Rect(r_paddle_pos, paddle_size))
    pygame.draw.rect(screen, (255,255,255), Rect(l_paddle_pos, paddle_size))
    
    ball.move()
    ball.draw()
    
    # unlock the screen
    screen.unlock()
    
    # call update to redraw the screen    
    pygame.display.update()
    
    
    
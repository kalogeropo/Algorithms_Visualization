#Author: Nikitas Rigas Kalogeropoulos
#This is a python sorting algorithms visualization tool done for exercise purpose
import pygame

#init pygame
pygame.init()

#grid dimentions width*width
width = 600
screen = pygame.display.set_mode((width, width))
caption= pygame.display.set_caption('SAV: Sorting Algorithm Visualization')

#Colors RGB:
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
yellow = (255,255,0)

background_colour = (192,192,192)

screen.fill(background_colour)
pygame.display.flip()


#main loop
exit_flag = True
while exit_flag:
    #Handling pressing X event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit_flag = False



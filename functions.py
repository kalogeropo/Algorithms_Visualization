import pygame
def init():
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


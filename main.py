#Author: Nikitas Rigas Kalogeropoulos
#This is a python sorting algorithms visualization tool done for exercise purpose
import pygame
from functions import *

init()

#main loop
exit_flag = True
while exit_flag:
    #Handling pressing X event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit_flag = False



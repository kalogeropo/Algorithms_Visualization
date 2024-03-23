import pygame

WIDTH = 500
TOT_ROW = 10
colour_map = {'A': (255, 0, 0),  # default
              'B': (197, 147, 49),
              'C': (130, 168, 49),  # closed
              'O': (52, 175, 137),  # opened
              'E': (55, 170, 186),  # end
              'S': (128, 150, 244),  # Start
              'G': (244, 93, 235),
              "BLACK": (0, 0, 0)}  # Wall
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

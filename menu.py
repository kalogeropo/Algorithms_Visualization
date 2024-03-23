import pygame

from properties import WIDTH, colour_map, screen, clock, TOT_ROW
from utils import Button
from visualise import main

pygame.init()
pygame.display.set_caption("Algorithm Visualizations Menu")
font = pygame.font.Font(pygame.font.get_default_font(),24)
main_menu = True
run = True



def draw_main_menu():
    pfa_btn = Button(screen,'Path Finding Algorithms',font,100,100,300,40,) #5,8
    pfa_btn.draw_button(5,8)

    srt_btn = Button(screen,'Sorting Algorithms',font,100,200,300,40 )
    srt_btn.draw_button(35,8)
    exit_btn = Button(screen,'Exit',font,100,400,300,40)
    exit_btn.draw_button(120,8)

    if pfa_btn.checked_clicked(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        return (True,1)
    if srt_btn.checked_clicked(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        return (True,2)
    if exit_btn.checked_clicked(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        return (False,0)
    return True, -1


while run:
    screen.fill(colour_map["G"])
    clock.tick(60)

    if main_menu:
        run,menu = draw_main_menu()
        if menu>0:
            main_menu = False
    else:
        # TODO: Implement Sorting algorithms
        # TODO: Screen for width and rows inputs
        # TODO: Implement a sub menu for more sorting algorithms
        if menu == 2:
            print("Sorting")
        # TODO: Implement a sub menu for more pathfinding algorithms
        # TODO: Screen for width and rows inputs
        if menu == 1:
            print("Sorting")
            print("Path Finding Algorithms")
            pygame_window = pygame.display.set_mode((WIDTH, WIDTH))
            pygame.display.set_caption("A - star")

            print(WIDTH, TOT_ROW)
            main(pygame_window, WIDTH, TOT_ROW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
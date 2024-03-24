from time import sleep

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
    pfa_btn = Button(screen,'A-Star',font,100,50,300,40,) #5,8
    pfa_btn.draw_button(110,8)

    srt_btn = Button(screen,'Empty Slot',font,100,100,300,40 )
    srt_btn.draw_button(80,8)

    btn1 = Button(screen, 'Empty Slot', font, 100, 150, 300, 40)
    btn1.draw_button(80, 8)

    btn2 = Button(screen, 'Empty Slot', font, 100, 200, 300, 40)
    btn2.draw_button(80, 8)

    btn3 = Button(screen, 'Empty Slot', font, 100, 250, 300, 40)
    btn3.draw_button(80, 8)

    btn4 = Button(screen, 'Empty Slot', font, 100, 300, 300, 40)
    btn4.draw_button(80, 8)
    btn5 = Button(screen, 'Empty Slot', font, 100, 350, 300, 40)
    btn5.draw_button(80, 8)
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

        if menu == 1:
            print("Astar") #TODO: Clear Board after algorithm ends

            instructions_end = True
            text = "0"
            text_surf = font.render(text, True, (255, 0, 0))
            text_surf_inp = text_surf.get_rect()

            input_active = True
            while instructions_end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            instructions_end = False
                        elif input_active:
                            if event.key == pygame.K_RETURN:
                                input_active = False
                            elif event.key == pygame.K_BACKSPACE:
                                screen.fill(colour_map["G"])
                                text = text[:-1]
                            else:
                                if event.unicode.isnumeric():
                                    text += event.unicode
                    text_surf = font.render(text, True, [255, 87, 51], [69, 169, 169])
                    text_surf_inp = text_surf.get_rect()
                    text_surf_inp.center = (WIDTH // 3, WIDTH // 5)
                    details = font.render('Instruction Set Here!',True, [255, 87, 51], [69, 169, 169])

                    textRect = details.get_rect()
                    textRect.center = (WIDTH // 2, WIDTH // 3)

                    screen.blit(text_surf,text_surf_inp )
                    screen.blit(details, textRect)
                    pygame.display.flip()
            if int(text) <= WIDTH:
                WIDTH = int(text)
            pygame_window = pygame.display.set_mode((WIDTH, WIDTH))
            pygame.display.set_caption("A - star")

            print(WIDTH, TOT_ROW)
            main(pygame_window, WIDTH, TOT_ROW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
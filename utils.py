import pygame

from properties import colour_map

class Button:
    def __init__(self,screen,text,font,x,y,w,h):
        self.screen = screen
        self.text = text
        self.button = pygame.rect.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
    def draw_button(self, offset_x,offset_y):
        pfa_btn = pygame.draw.rect(self.screen, 'light gray', [self.x,self.y,self.w,self.h], 0, 5)
        pygame.draw.rect(self.screen, 'dark gray', [self.x,self.y,self.w,self.h], 5, 5)
        text = self.font.render(self.text, True, colour_map['B'])
        self.screen.blit(text, (self.x+offset_x, self.y+offset_y))
        return pfa_btn

    def checked_clicked(self, param):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            #print("pressed")
            return True
        else:
            return False
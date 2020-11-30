import pygame
from pygame.locals import *

#Incializar o pygame
pygame.init()

#Criar uma classe com as características dos botões
class ButtonABCDE:
    #Criar o botão
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    #Texto do botão
    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = 15
        myFont = pygame.font.SysFont("Arial", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    #Desenhar o botão
    def draw_button(self, surface, color, length, height, x, y, width):           
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, color, (x,y,length,height), 0)  
        return surface

    #Definição do botão pressionado
    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print ("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

#--------------------------------------------------------------------------------------------------------------
class Button:
    #Criar o botão
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    #Texto do botão
    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = 30
        myFont = pygame.font.Font("fonts/Franchise.ttf", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    #Desenhar o botão
    def draw_button(self, surface, color, length, height, x, y, width):           
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, color, (x,y,length,height), 0)  
        return surface

    #Definição do botão pressionado
    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print ("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

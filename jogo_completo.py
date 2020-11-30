#importações
import pygame, Buttons
from pygame.locals import *
from perguntas import *
import textwrap
import fonts

#Inicializar o pygame
pygame.init()

#Alguns parâmetros
porcentagem_certas = ""
porcentagem_erradas = ""
tamanho = [] 
respostas = []
respostas1 =[]
respostas2 =[]
certa = []
errada = []
clock = pygame.time.Clock()
FPS=30

#dimensões da tela
screen_width=950
screen_height=650
screen=pygame.display.set_mode((screen_width, screen_height))

#Fontes
font = pygame.font.Font("fonts/RobotoSlab-Regular.ttf", 22)
font_menu_title = pygame.font.Font("fonts/maus.ttf", 100)
font_menu_subtitle = pygame.font.Font("fonts/BowlbyOneSC-Regular.ttf", 50)
font_menu_opcoes = pygame.font.Font("fonts/maus.ttf", 45)
font_alt = pygame.font.Font("fonts/RobotoSlab-Regular.ttf", 18)
#font_title = pygame.font.SysFont("fonts/BowlbyOneSC-Regular.ttf", 90)
fonte = "Agency FB"
font_title = pygame.font.Font("fonts/maus.ttf", 60)
#Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

#Texto
def text_format(message, textFont, font_size, textColor):
    newFont=pygame.font.SysFont(textFont, font_size)
    newText=newFont.render(message, 0, textColor)
    return newText

class Menu:
    def main_menu():
    
        menu=True
        selected="iniciar"
    
        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="iniciar"
                    if event.key==pygame.K_DOWN:
                        selected="sobre"
                    if event.key==pygame.K_RETURN:
                        if selected=="iniciar":
                            Jogo()
                        if selected=="sobre":
                            Instrucao()

            # Opções de Menu
            fundo = pygame.image.load('fundorosa.jpg')
            screen.blit(fundo, [0,0])
            title = font_menu_title.render("ENEMStudiesQuiz", True, preto)
            
            if selected=="iniciar":
                pygame.draw.rect(screen, (249,125,95), [375 , 245, 200, 70])
                text_iniciar=font_menu_opcoes.render("INICIAR", True, preto)
            else:
                pygame.draw.rect(screen, preto, [375 , 245, 200, 70])
                text_iniciar = font_menu_opcoes.render("INICIAR", True, (249,125,95))
                
            if selected=="sobre":
                pygame.draw.rect(screen, (249,125,95), [375 , 320, 200, 70])
                text_sobre=font_menu_opcoes.render("SOBRE", True, preto)
            else:
                pygame.draw.rect(screen, preto, [375 , 320, 200, 70])
                text_sobre = font_menu_opcoes.render("SOBRE", True, (249,125,95))
            
            title_rect=title.get_rect()
            iniciar_rect=text_iniciar.get_rect()
            sobre_rect=text_sobre.get_rect()

    
            # Configurações do Texto
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
            screen.blit(text_iniciar, (screen_width/2 - (iniciar_rect[2]/2), 250))
            screen.blit(text_sobre, (screen_width/2 - (sobre_rect[2]/2), 330))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("ENEMStudiesQuiz")


class Instrucao:
    def __init__(self):
        self.main()
    
    #Cria a tela
    def display(self):
        self.screen = pygame.display.set_mode((950,620))
        pygame.display.set_caption("ENEMStudiesQuiz")
        fundorosa = pygame.image.load('fundorosa.jpg')
        screen.blit(fundorosa, [0,0])

        titulo1 = font_title.render("INSTRUÇÕES DO JOGO", True, preto)
        texto1 = font.render("- Para jogar, basta clicar no botão correspondente a resposta correta.", True, preto)
        texto2 = font.render("- Sua pontuação será exibida no final, portanto não saia do jogo.", True, preto)
        titulo2 = font_title.render("CRIAÇÃO", True, preto)
        texto3 = font.render("- Este jogo foi criado na disciplina de Projeto Integrador, ", True, preto)
        texto4 = font.render("por alunas do curso Técnico em Informática integrado ao Ensino Médio", True, preto)
        texto5 = font.render("do Instituto Federal Catarinense - Campus Blumenau", True, preto)
        texto6 = font.render("- Priscila Lemke e Vanessa de Souza", True, preto)
        
        title1_rect=titulo1.get_rect()
        texto1_rect=texto1.get_rect()
        texto2_rect=texto2.get_rect()
        title2_rect=titulo2.get_rect()
        texto3_rect=texto3.get_rect()
        texto4_rect=texto4.get_rect()
        texto5_rect=texto5.get_rect()
        texto6_rect=texto6.get_rect()
        self.screen.blit(titulo1, [screen_width/2 - (title1_rect[2]/2), 40],)
        screen.blit(texto1, (screen_width/2 - (texto1_rect[2]/2), 120))
        screen.blit(texto2, (screen_width/2 - (texto2_rect[2]/2), 170))
        self.screen.blit(titulo2, [screen_width/2 - (title2_rect[2]/2), 210],)
        screen.blit(texto3, (screen_width/2 - (texto3_rect[2]/2), 300))
        screen.blit(texto4, (screen_width/2 - (texto4_rect[2]/2), 340))
        screen.blit(texto5, (screen_width/2 - (texto5_rect[2]/2), 380))
        screen.blit(texto6, (screen_width/2 - (texto6_rect[2]/2), 420))
        self.Buttonmenu = Buttons.Button()
        #Parâmetros:                 surface,   color,   x,   y, length, height, width,  text,    text_color
        self.Buttonmenu.create_button(self.screen, (249,125,95), 375, 500, 200,    50,    0,     " Voltar ao Menu ", (0,0,0))
        pygame.display.flip()

    #Função do botão
    def main(self):
        self.display()
        while True:
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Buttonmenu.pressed(pygame.mouse.get_pos()):
                        Menu.main_menu()

  
lista = len(questoes)-1
class Jogo:
    
    #Resultados
    def fim(self):
        gabarito = ['A', 'C', 'C', 'E', 'C', 'C', 'E', 'C', 'B', 'B', 'C', 'D', 'A', 'A', 'D', 'D', 'A', 'D',
         'D', 'B', 'E', 'A', 'B', 'C', 'B', 'B', 'C', 'D', 'E', 'B', 'C', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'E', 'C']
        for i in range(len(gabarito)):
            if gabarito[i] == respostas[i]:
                certa.append(respostas[i])
            elif gabarito[i] != respostas[i]:
                errada.append(respostas[i])    
        Resultado()

    def __init__(self):
        self.main()
    
    #Cria a tela
    def display(self):
        self.screen = pygame.display.set_mode((950,620))
        pygame.display.set_caption("ENEMStudiesQuiz")
    
    #Atualiza a tela e mostra os botões
    def update_display(self):
        n = len(tamanho)
        if n <= lista:
            fundorosa = pygame.image.load('fundorosa.jpg')
            screen.blit(fundorosa, [0,0])
            questao = textwrap.fill(questoes[n], 80)
            h = 30
            lin = 0
            for parte in questao.split('\n'):
                q = font.render(parte, True, preto)
                self.screen.blit(q, [50,h+lin],)
                lin += 25

            #Parâmetros:                 surface,   color,   x,   y, length, height, width,  text,    text_color
            self.Button1.create_button(self.screen, (0, 0, 0), 50, (h + lin + 20), 50,    29,    0,      " A ", (255,255,255))
            a = font_alt.render(alternativas_a[n], True, preto)
            self.screen.blit(a, [120,(h + lin + 25)],)

            self.Button2.create_button(self.screen, (0, 0, 0), 50, (h + lin + 60), 50,    29,    0,      " B ", (255,255,255))
            b = font_alt.render(alternativas_b[n], True, preto)
            self.screen.blit(b, [120,(h + lin + 65)],)

            self.Button3.create_button(self.screen, (0, 0, 0), 50, (h + lin + 100), 50,    29,    0,      " C ", (255,255,255))
            c = font_alt.render(alternativas_c[n], True, preto)
            self.screen.blit(c, [120,(h + lin + 105)],)
            
            self.Button4.create_button(self.screen, (0, 0, 0), 50, (h + lin + 140), 50,    29,    0,     " D ", (255,255,255))
            d = font_alt.render(alternativas_d[n], True, preto)
            self.screen.blit(d, [120,(h + lin + 145)],) 

            self.Button5.create_button(self.screen, (0, 0, 0), 50, (h + lin + 180), 50,    29,    0,     " E ", (255,255,255))
            e = font_alt.render(alternativas_e[n], True, preto)
            self.screen.blit(e, [120,(h + lin + 185)],) 
        
            pygame.display.flip()
        
        else:
            self.fim()

    #Mostra qual botão foi clicado
    def main(self):
        self.Button1 = Buttons.ButtonABCDE()
        self.Button2 = Buttons.ButtonABCDE()
        self.Button3 = Buttons.ButtonABCDE()
        self.Button4 = Buttons.ButtonABCDE()
        self.Button5 = Buttons.ButtonABCDE()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        respostas.append("A")
                        print (respostas) 
                        tamanho.append("valor")
                        self.update_display()
                    elif self.Button2.pressed(pygame.mouse.get_pos()):
                        respostas.append("B")
                        print(respostas)
                        tamanho.append("valor")
                        self.update_display()
                    elif self.Button3.pressed(pygame.mouse.get_pos()):
                        respostas.append("C")
                        print(respostas)
                        tamanho.append("valor")
                        self.update_display()
                    elif self.Button4.pressed(pygame.mouse.get_pos()):
                        respostas.append("D")
                        print(respostas)
                        tamanho.append("valor")
                        self.update_display()
                    elif self.Button5.pressed(pygame.mouse.get_pos()):
                        respostas.append("E")
                        print(respostas)
                        tamanho.append("valor")
                        self.update_display()
                    



class Resultado:
    def __init__(self):
        self.main()
    
    #Cria a tela
    def display(self):
        self.screen = pygame.display.set_mode((950,620))
        pygame.display.set_caption("ENEMStudiesQuiz")


    def main_gabarito(self):
        gabarito1 = ['A', 'C', 'C', 'E', 'C', 'C', 'E', 'C', 'B', 'B', 'C', 'D', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'B']
        gabarito2 = ['E', 'A', 'B', 'C', 'B', 'B', 'C', 'D', 'E', 'B', 'C', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'E', 'C']
        respostas1.append(respostas[0:20])
        respostas2.append(respostas[20:40])
        fundorosa = pygame.image.load('fundorosa.jpg')
        self.screen.blit(fundorosa, [0,0])
        titulo = font_title.render("GABARITO", True, preto)
        texto1 = font.render("O gabarito é " + str(gabarito1), True, preto)
        texto1_2 = font.render(str(gabarito2), True, preto)
        texto2 = font.render("As respostas foram " + str(respostas1), True, preto)
        texto2_2 = font.render(str(respostas2), True, preto)
        title_rect=titulo.get_rect()
        texto1_rect=texto1.get_rect()
        texto1_2_rect = texto1_2.get_rect()
        texto2_rect=texto2.get_rect()
        texto2_2_rect = texto2_2.get_rect()
        screen.blit(titulo, (screen_width/2 - (title_rect[2]/2), 60))
        screen.blit(texto1, (screen_width/5 - (title_rect[2]/2), 160))
        screen.blit(texto1_2, (screen_width/5 - (title_rect[2]/2), 200))
        screen.blit(texto2, (screen_width/5 - (title_rect[2]/2), 240))
        screen.blit(texto2_2, (screen_width/5 - (title_rect[2]/2), 280))
        pygame.display.update()
        self.display()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

    #Atualiza a tela 
    def update_display(self):
        gabarito = ['A', 'C', 'C', 'E', 'C', 'C', 'E', 'C', 'B', 'B', 'C', 'D', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'B', 'E', 'A', 'B', 'C', 'B', 'B', 'C', 'D', 'E', 'B', 'C', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'E', 'C']
        porcentagem_certas = str((len(certa)*100)/len(gabarito))
        porcentagem_erradas = str((len(errada)*100)/len(gabarito))
        fundorosa = pygame.image.load('fundorosa.jpg')
        screen.blit(fundorosa, [0,0])
        titulo = font_title.render("RESULTADOS", True, preto)
        texto1 = font.render("A quantidade de respostas certas foi de " + str(porcentagem_certas) + "%", True, preto)
        texto2 = font.render("A quantidade de respostas erradas foi de " + str(porcentagem_erradas) + "%", True, preto)
        title_rect=titulo.get_rect()
        texto1_rect=texto1.get_rect()
        texto2_rect=texto2.get_rect()
        screen.blit(titulo, (screen_width/2 - (title_rect[2]/2), 60))
        screen.blit(texto1, (screen_width/2.3 - (title_rect[2]/2), 160))
        screen.blit(texto2, (screen_width/2.3 - (title_rect[2]/2), 200))
        self.Buttongabarito = Buttons.Button()
        self.Buttongabarito.create_button(self.screen, (0, 0, 0), 375, 370, 200,    50,    0,     " Ver gabarito ", (255,255,255))
        pygame.display.flip()
 
    
 
    #Função do botão
    def main(self):
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Buttongabarito.pressed(pygame.mouse.get_pos()):
                        self.main_gabarito()



#Inicializa o jogo
Menu.main_menu()



if __name__ == '__main__':
    Menu.main_menu()
    

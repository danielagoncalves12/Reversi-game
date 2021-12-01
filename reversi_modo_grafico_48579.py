# ISEL - LEIM
#
# Jogo Reversi Interface gráfica
#
# Daniela Gonçalves - A48579 11D-A

import pygame
from pygame.locals import *

from reversi_motor_48579 import reversi_novo_jogo
from reversi_motor_48579 import reversi_valor
from reversi_motor_48579 import reversi_jogada_possivel
from reversi_motor_48579 import reversi_fim_jogo
from reversi_motor_48579 import reversi_proximo_a_jogar
from reversi_motor_48579 import reversi_pontuacao
from reversi_motor_48579 import reversi_jogar

from reversi_agente_48579 import jogada_agente

pygame.mixer.init()
pygame.mixer.pre_init(44100,16,2,4096) # Iniciação do mixer (frequencia, bits, saidas, buffer)
pygame.init()


background = pygame.image.load("imgs/background.bmp")
jogadorX = pygame.image.load("imgs/jogadorX.png")
jogadorO = pygame.image.load("imgs/jogadorO.png")
jogada  = pygame.image.load("imgs/jogada.png")
inicio_msg = pygame.image.load("imgs/tutorial.png");

# Criar uma janela gráfica:

size    = [850,700]  # tamanho da janela
screen  = pygame.display.set_mode(size)  # abrir janela
pygame.display.set_caption("Jogo Reversi - Daniela Gonçalves") # nome da janela
clock = pygame.time.Clock()

# Cores e tamanhos:

grey  = (40,40,40)
white = (255,255,255)
red   = (255,0,0)


global simbolo_primeiro_a_jogar
global simbolo_segundo_a_jogar
simbolo_primeiro_a_jogar = None
simbolo_segundo_a_jogar  = None


# formatar tipos de texto

def texto (pos, txt, color, f_size, bg_color):
    
    font = pygame.font.Font(None, f_size)
    text = font.render(txt,True,color,bg_color)
    screen.blit(text, pos) # blit inserir imagens sobre outras
    

def print_grelha_grafica(jogo):
    
    yi=100
    for linha in [1,2,3,4,5,6,7,8]:
        xi=179
        for coluna in [1,2,3,4,5,6,7,8]:
            
            if converter_valor(reversi_valor(jogo, linha, coluna)) == 'Preta':
                screen.blit(jogadorX,[xi,yi])
    
            if converter_valor(reversi_valor(jogo, linha, coluna)) == 'Branca':
                screen.blit(jogadorO,[xi,yi])
                
            xi+=61
        yi+=61


def print_jogadas(jogo):

    yi=100
    for linha in [1,2,3,4,5,6,7,8]:
        xi=179
        for coluna in [1,2,3,4,5,6,7,8]:

            if reversi_jogada_possivel(jogo, linha, coluna):
                screen.blit(jogada,[xi,yi])
                
            xi+=61
        yi+=61



def converter_valor(valor):

    if valor == 0:
        return ' '
    if valor == 1:
        return simbolo_primeiro_a_jogar
    if valor == 2:
        return simbolo_segundo_a_jogar




def print_vencedor(jogo):

    pontos = reversi_pontuacao(jogo)

    if pontos[0] > pontos[1]:
        texto((250,400),"Jogador de peça "+converter_valor(1)+" GANHOU!",red,34,None)
    elif pontos[0] < pontos[1]:
        texto((250,400),"Jogador de peça "+converter_valor(2)+" GANHOU!",red,34,None)
    else:
        texto((250,400),"EMPATE!",red,34,None)



def jogada_jogador(jogo):

    nao_escreveu_linha = True
    nao_escreveu_coluna = True
    linha = None
    coluna = None

    
    while nao_escreveu_linha:
        
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if (event.key == K_1):
                        linha = 1
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_2):
                        linha = 2
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_3):
                        linha = 3
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_4):
                        linha = 4
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_5):
                        linha = 5
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_6):
                        linha = 6
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_7):
                        linha = 7
                        nao_escreveu_linha = False
                        
                    elif (event.key == K_8):
                        linha = 8
                        nao_escreveu_linha = False
                        
                    else:
                        linha = None
                        nao_escreveu_linha = True
                        
    texto((395,645),str(linha),grey,32,None)
    pygame.display.flip()
                        
    while nao_escreveu_coluna:
        
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if (event.key == K_1):
                        coluna = 1
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_2):
                        coluna = 2
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_3):
                        coluna = 3
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_4):
                        coluna = 4
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_5):
                        coluna = 5
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_6):
                        coluna = 6
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_7):
                        coluna = 7
                        nao_escreveu_coluna = False
                        
                    elif (event.key == K_8):
                        coluna = 8
                        nao_escreveu_coluna = False
                        
                    else:
                        coluna = None
                        nao_escreveu_coluna = True
                        
    texto((535,645),str(coluna),grey,32,None)
    pygame.display.flip()             
 
    
    return (linha, coluna)




jogo = reversi_novo_jogo()
inicio = True
escolher = True
continuar = False

ordem = ""
escolha = ""

## CICLO LOOP do JOGO
while not reversi_fim_jogo(jogo):


    pygame.event.get()
 
    if inicio == True:
        screen.blit(inicio_msg, (220, 140))
        
        if escolher == True:      
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                
                    if (event.key == K_x):
                        escolha = "Preta"
                        texto((320,550),"Peça: "+escolha,white,40,None)
                        continuar = True
                        escolher = False
                    
                    elif (event.key == K_o):
                        escolha = "Branca"
                        texto((320,550),"Peça: "+escolha,white,40,None)                       
                        continuar = True
                        escolher = False
                    
                    elif (event.key == K_RETURN):
                        escolha = "Preta"
                        texto((320,550),"Peça: "+escolha,white,40,None)
                        continuar = True
                        escolher = False  

        if continuar == True:
            
            for event in pygame.event.get():     
                if event.type == KEYDOWN:
                    
                    if (event.key == K_1):
                        ordem = '1'
                        texto((320,580),ordem+" a jogar",white,40,None)
                        inicio = False
                        
                    elif (event.key == K_2):
                        ordem = '2'
                        texto((320,580),ordem+" a jogar",white,40,None)
                        inicio = False
                        
                    elif (event.key == K_RETURN):
                        ordem = '1'
                        texto((320,580),ordem+" a jogar",white,40,None)
                        inicio = False
                        
        if ordem == '1':
            
            if escolha == 'Preta':
                
                simbolo_primeiro_a_jogar = 'Preta'
                simbolo_segundo_a_jogar  = 'Branca'
                
            elif escolha == 'Branca':
                
                simbolo_primeiro_a_jogar = 'Branca'
                simbolo_segundo_a_jogar  = 'Preta'
                
        elif ordem == '2':
            
            if escolha == 'Preta':
                
                simbolo_primeiro_a_jogar = 'Branca'
                simbolo_segundo_a_jogar  = 'Preta'
                
            elif escolha == 'Branca':
                
                simbolo_primeiro_a_jogar = 'Preta'
                simbolo_segundo_a_jogar  = 'Branca'
                    
 
    else:

        ## Print tabuleiro        
        screen.blit(background,(0, 0))
        print_grelha_grafica(jogo)
        print_jogadas(jogo)
        pontos = reversi_pontuacao(jogo)
        texto((170,25),str(pontos[0]),grey,40,None)
        texto((780,25),str(pontos[1]),grey,40,None)
        
        (proximo_a_jogar, jogador_que_passou) = reversi_proximo_a_jogar(jogo)

        #if jogador_que_passou != None:
            #texto((250,400),'Quem joga com '+str(converter_valor(jogador_que_passou))+' não tinha como jogar. PASSOU!!!',blue,32,None)
        
        texto((215,645),str(proximo_a_jogar),grey,32,None)

        
        if proximo_a_jogar == 1:
            if converter_valor(proximo_a_jogar) == 'Preta':
                screen.blit(jogadorX,[40,550])
            else:
                screen.blit(jogadorO,[40,550])

        if proximo_a_jogar == 2:
            if converter_valor(proximo_a_jogar) == 'Branca':
                screen.blit(jogadorO,[40,550])
            else:
                screen.blit(jogadorX,[40,550])         

        pygame.display.flip() 
        
        if proximo_a_jogar == int(ordem):

            (linha, coluna) = jogada_jogador(jogo)
            #(linha, coluna) = jogada_agente(jogo)

        else:
            pygame.time.delay(1000)
            (linha, coluna) = jogada_agente(jogo)
            
            texto((395,645),str(linha),grey,32,None)
            texto((535,645),str(coluna),grey,32,None)
            pygame.display.flip()

        pygame.time.delay(1000)
        
        jogo = reversi_jogar(jogo, linha, coluna)


        print_grelha_grafica(jogo)
        print_jogadas(jogo)
        #clock.tick(0)
        pygame.display.flip()
        

            
    pygame.display.flip()


print_vencedor(jogo)
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()

import sys
import random
from reversi_motor_48579 import reversi_jogada_possivel

def jogada_agente(jogo):

    linha = random.randint(1,8)
    coluna = random.randint(1,8)
    verificacao = reversi_jogada_possivel(jogo, linha, coluna)
   
    if (verificacao == True):
        return (linha, coluna)
    else:
        return jogada_agente(jogo)

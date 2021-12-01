def reversi_novo_jogo():  

    grelha = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

    #Constantes
    PRIMEIRO_JOGADOR_A_JOGAR = 1
    SEGUNDO_JOGADOR_A_JOGAR = 2

    #Variaveis
    fim = False
    proximo_a_jogar = PRIMEIRO_JOGADOR_A_JOGAR
    jogador_que_passou = SEGUNDO_JOGADOR_A_JOGAR

    #Retorno novo jogo
    jogo = [grelha, fim, proximo_a_jogar, jogador_que_passou]
    return jogo





def reversi_obter_valor_na_grelha(grelha, linha, coluna):

    if not (linha >= 0 and linha <= 7 and coluna >= 0 and coluna <=7):
        return None
    else:
        return grelha[linha][coluna]




def reversi_valor(jogo, linha, coluna): 

    grelha = jogo[0]
    valor = reversi_obter_valor_na_grelha(grelha, linha-1, coluna-1)

    if valor   == 0:
        return 0
    elif valor == 1:
        return 1
    elif valor == 2:
        return 2
    else:
        return None





def reversi_jogada_possivel(jogo, linha, coluna): 

    (grelha, fim, proximo_a_jogar, jogador_que_passou) = jogo

    jogadas_possiveis = []
    tem_movimentos_validos = reversi_verificar_movimento(grelha, proximo_a_jogar, linha-1, coluna-1)

    if tem_movimentos_validos == True:
        jogadas_possiveis.append([linha,coluna])
    else:
        jogadas_possiveis = []
    
    if len(jogadas_possiveis) != 0:
        return True
    else:
        return False






def reversi_listar_jogadas_possiveis(jogo, proximo_a_jogar): ## Listar todas as jogadas possiveis no momento para um certo jogador

    grelha = jogo[0]
    lista_com_jogadas = []

    for indice_linha in range(len(grelha)):
        for indice_coluna in range(len(grelha[0])):
            verificar = reversi_verificar_movimento(grelha, proximo_a_jogar, indice_linha, indice_coluna)

            if verificar == True:
                lista_com_jogadas.append([indice_linha+1,indice_coluna+1])

    return lista_com_jogadas






def reversi_verificar_movimento(grelha, jogador, linha, coluna):  ## Retorna True se houver peças para virar, ou seja a linha x e coluna x é um movimento valido
    
    pecas_para_virar = []
    DIRECOES = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]


    if grelha[linha][coluna] == 0:
        for indice in range(len(DIRECOES)):
            
            direcao_escolhida = DIRECOES[indice]        
            sequencia = reversi_get_sequencia(grelha, jogador, linha, coluna, direcao_escolhida[0], direcao_escolhida[1])
            
            if sequencia != None:
                pecas_para_virar = pecas_para_virar + sequencia

    if len(pecas_para_virar) > 0:
        return True
    else:
        return False





def reversi_get_sequencia(grelha, jogador, linha, coluna, direcao_v, direcao_h):
    
    pecas_para_virar = []
    outro = obter_o_outro_jogador(jogador)

    ## Fora da grelha
    if (linha + direcao_v > 7) or (linha + direcao_v < 0) or (coluna + direcao_h < 0) or (coluna + direcao_h > 7):
        return None

    ## Se à volta da nossa peça achar uma peça adversária
    if grelha[linha + direcao_v][coluna + direcao_h] == outro:

        ## Adiciona essa peça à lista
        pecas_para_virar.append([linha + 1 + direcao_v, coluna + 1 + direcao_h])


        ## Verificar se ha mais peças adversarias aseguir à anterior
        for indice in range(1,9):
         
            if (linha + direcao_v * indice > 7) or (linha + direcao_v * indice < 0) or (coluna + direcao_h * indice < 0) or (coluna + direcao_h * indice > 7):
                return None
            
            if grelha[linha + direcao_v * indice][coluna + direcao_h * indice] == outro:
                pecas_para_virar.append([linha + 1 + direcao_v * indice, coluna + 1 + direcao_h * indice])

            if grelha[linha + direcao_v * indice][coluna + direcao_h * indice] == 0:
                return None
            
            if grelha[linha + direcao_v * indice][coluna + direcao_h * indice] == jogador:
                return pecas_para_virar
            



def reversi_get_linhas_vazias(grelha): ## Verificar se ainda há espaços em branco

    posicoes_vazias = []
    
    for linha in grelha:
            if 0 in linha:
                posicoes_vazias.append(linha)

    return posicoes_vazias





def reversi_fim_jogo(jogo):  ## Deteta se o jogo acabou

    (grelha, final, proximo_a_jogar, jogador_que_passou) = jogo

    posicoes_vazias = reversi_get_linhas_vazias(grelha)
    
    outro = obter_o_outro_jogador(proximo_a_jogar) 
    lista_movimentos_proximo = reversi_listar_jogadas_possiveis(jogo, proximo_a_jogar)
    lista_movimentos_outro = reversi_listar_jogadas_possiveis(jogo, outro)

    if len(posicoes_vazias) == 0:
        return True

    if len(lista_movimentos_proximo) == 0:
        if len(lista_movimentos_outro) == 0:
            print("Ambos os jogadores X e O sem opções para jogar.")
            return True

    return False





def obter_o_outro_jogador(jogador):  # Recebendo um certo jogador, retorna o outro

    if(jogador == 1):
        return 2
    
    elif(jogador == 2):
        return 1





def reversi_proximo_a_jogar(jogo):   ## Retorna o proximo jogador a jogar e se houve algum jogador sem jogadas

    (grelha, fim, jogador, jogador_que_passou) = jogo
    outro = obter_o_outro_jogador(jogador)

    if(fim == True):
        proximo_a_jogar = None
    else:
        proximo_a_jogar = jogador

    lista_movimentos_proximo = reversi_listar_jogadas_possiveis(jogo, proximo_a_jogar)
    
    if len(lista_movimentos_proximo) == 0:    
        jogador_que_passou = jogador
        proximo_a_jogar = outro

    else:
        jogador_que_passou = None
        proximo_a_jogar = jogador

    jogo[2] = proximo_a_jogar
    jogo[3] = jogador_que_passou

    return (proximo_a_jogar, jogador_que_passou)





def reversi_pontuacao(jogo):  ## Retorna a pontuacao de ambos os jogadores

    grelha = jogo[0]
    pontos_jogador_1 = 0
    pontos_jogador_2 = 0

    #Percorre a grelha e soma os pontos
    for indice_linha in range(8):
        for indice_coluna in range(8):

            if grelha[indice_linha][indice_coluna] == 1:
                pontos_jogador_1 += 1
            if grelha[indice_linha][indice_coluna] == 2:
                pontos_jogador_2 += 1

    return (pontos_jogador_1, pontos_jogador_2)





def reversi_alterar_valor_grelha(grelha, linha, coluna, proximo_a_jogar):  ## Funcao auxiliar para alterar o valor de um elemento da grelha

    grelha[linha][coluna] = proximo_a_jogar




def reversi_jogar(jogo, linha, coluna):   ## Se o movimento for valido, joga a peça numa certa linha e coluna

    #Variaveis
    (grelha, fim, proximo_a_jogar, jogador_que_passou) = jogo
    pecas_para_virar=[]

    #Contantes
    DIRECOES = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]

    verificacao = reversi_jogada_possivel(jogo, linha, coluna)

    if verificacao == False:
        
        print("Movimento inválido")
        return jogo
        
    else:

        for indice in range(len(DIRECOES)):
            
            direcao_escolhida = DIRECOES[indice]
            sequencia = reversi_get_sequencia(grelha, proximo_a_jogar, linha-1, coluna-1, direcao_escolhida[0], direcao_escolhida[1])
            
            if sequencia != None:
                pecas_para_virar = pecas_para_virar + sequencia


        # Coloca a peça no local escolhido e vira as outras peças adversarias

        reversi_alterar_valor_grelha(grelha, linha-1, coluna-1, proximo_a_jogar)

        for elemento in pecas_para_virar:
            reversi_alterar_valor_grelha(grelha, elemento[0]-1, elemento[1]-1, proximo_a_jogar)
     


        # Jogada feita, Proximo a jogar vai ser o outro jogador
        
        proximo_a_jogar = obter_o_outro_jogador(proximo_a_jogar)
        jogo_atualizado = [grelha, fim, proximo_a_jogar, jogador_que_passou]

        print("Movimento válido")
        return jogo_atualizado

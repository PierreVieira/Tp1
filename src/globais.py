from OpenGL.GLUT import *
import time
import pygame


def text_e(imgload):
    img = pygame.image.tostring(imgload, 'RGBA', 1)
    return img


aux_musica = True
imgload = []
img = []
imgload.append(pygame.image.load('files/images/Loli1_parte1.png'))
img.append(text_e(imgload[0]))
imgload.append(pygame.image.load('files/images/Loli2_parte1.png'))
img.append(text_e(imgload[1]))
imgload.append(pygame.image.load('files/images/Torre_tok.jpeg'))
img.append(text_e(imgload[2]))
imgload.append(pygame.image.load('files/images/menu_loli.jpg'))
img.append(text_e(imgload[3]))
imgload.append(pygame.image.load('files/images/play_button.png'))
img.append(text_e(imgload[4]))
imgload.append(pygame.image.load('files/images/Ranking_button.png'))
img.append(text_e(imgload[5]))
imgload.append(pygame.image.load('files/images/Kita_png.png'))
img.append(text_e(imgload[6]))
imgload.append(pygame.image.load('files/images/Instruções.png'))
img.append(text_e(imgload[7]))
imgload.append(pygame.image.load('files/images/Créditos_button.png'))
img.append(text_e(imgload[8]))
imgload.append(pygame.image.load('files/images/pause_fundo.png'))
img.append(text_e(imgload[9]))
imgload.append(pygame.image.load('files/images/menu_principal.png'))
img.append(text_e(imgload[10]))
imgload.append(pygame.image.load('files/images/mute_feito.png'))
img.append(text_e(imgload[11]))
imgload.append(pygame.image.load('files/images/sound_feito.png'))
img.append(text_e(imgload[12]))
imgload.append(pygame.image.load('files/images/quitar.png'))
img.append(text_e(imgload[13]))
imgload.append(pygame.image.load('files/images/LoliEncostou.png'))
img.append(text_e(imgload[14]))
imgload.append(pygame.image.load('files/images/desesperada.png'))
img.append(text_e(imgload[15]))
imgload.append(pygame.image.load('files/images/Yare.jpg'))
img.append(text_e(imgload[16]))
imgload.append(pygame.image.load('Danashi1-1.png'))
img.append(text_e(imgload[17]))

imgload.append(pygame.image.load('files/images/zero.png'))
img.append(text_e(imgload[18]))
imgload.append(pygame.image.load('files/images/one.png'))
img.append(text_e(imgload[19]))
imgload.append(pygame.image.load('files/images/two.png'))
img.append(text_e(imgload[20]))
imgload.append(pygame.image.load('files/images/three.png'))
img.append(text_e(imgload[21]))
imgload.append(pygame.image.load('files/images/four.png'))
img.append(text_e(imgload[22]))
imgload.append(pygame.image.load('files/images/five.png'))
img.append(text_e(imgload[23]))
imgload.append(pygame.image.load('files/images/six.png'))
img.append(text_e(imgload[24]))
imgload.append(pygame.image.load('files/images/seven.png'))
img.append(text_e(imgload[25]))
imgload.append(pygame.image.load('files/images/eight.png'))
img.append(text_e(imgload[26]))
imgload.append(pygame.image.load('files/images/nine.png'))
img.append(text_e(imgload[27]))
imgload.append(pygame.image.load('files/images/coracao.png'))
img.append(text_e(imgload[28]))
imgload.append(pygame.image.load('files/images/ranking.png'))
img.append(text_e(imgload[29]))
imgload.append(pygame.image.load('files/images/quitar.png'))
img.append(text_e(imgload[30]))
imgload.append(pygame.image.load('files/images/creditos.png'))
img.append(text_e(imgload[31]))
imgload.append(pygame.image.load('files/images/camburao.png'))
img.append(text_e(imgload[32]))
imgload.append(pygame.image.load('files/images/botao_borda.png'))
img.append(text_e(imgload[33]))
imgload.append(pygame.image.load('files/images/instrucoes.png'))
img.append(text_e(imgload[34]))
imgload.append(pygame.image.load('files/images/telaInicial.png'))
img.append(text_e(imgload[35]))
imgload.append(pygame.image.load('files/images/ganha_coracao.png'))
img.append(text_e(imgload[36]))
imgload.append(pygame.image.load('files/images/Ysaka.jpg'))
img.append(text_e(imgload[37]))
imgload.append(pygame.image.load('files/images/lolizinha2.png'))
img.append(text_e(imgload[38]))
imgload.append(pygame.image.load('files/images/lolizinha2two.png'))
img.append(text_e(imgload[39]))
imgload.append(pygame.image.load('files/images/lolizinha2_hited.png'))
img.append(text_e(imgload[40]))
imgload.append(pygame.image.load('files/images/lolizinha2_desesperada.png'))
img.append(text_e(imgload[41]))
imgload.append(pygame.image.load('files/images/ninjas.png'))
img.append(text_e(imgload[42]))
imgload.append(pygame.image.load('files/images/ninjas2.png'))
img.append(text_e(imgload[43]))
imgload.append(pygame.image.load('files/images/ninjas3.png'))
img.append(text_e(imgload[44]))
imgload.append(pygame.image.load('files/images/ninjas4.png'))
img.append(text_e(imgload[45]))
imgload.append(pygame.image.load('files/images/ninjas5.png'))
img.append(text_e(imgload[46]))
imgload.append(pygame.image.load('files/images/cats.jpg'))
img.append(text_e(imgload[47]))
imgload.append(pygame.image.load('files/images/brilhinhos.png'))
img.append(text_e(imgload[48]))
imgload.append(pygame.image.load('files/images/slash.png'))
img.append(text_e(imgload[49]))
imgload.append(pygame.image.load('files/images/botao_borda.png'))
img.append(text_e(imgload[50]))
imgload.append(pygame.image.load('files/images/ninjas_special3.png'))
img.append(text_e(imgload[51]))
imgload.append(pygame.image.load('files/images/ninjas_special5.png'))
img.append(text_e(imgload[52]))
imgload.append(pygame.image.load('files/images/um_1.png'))
img.append(text_e(imgload[53]))
imgload.append(pygame.image.load('files/images/dois_2.png'))
img.append(text_e(imgload[54]))
imgload.append(pygame.image.load('files/images/tres_3.png'))
img.append(text_e(imgload[55]))
imgload.append(pygame.image.load('files/images/quatro_4.png'))
img.append(text_e(imgload[56]))
imgload.append(pygame.image.load('files/images/cinco_5.png'))
img.append(text_e(imgload[57]))
imgload.append(pygame.image.load('files/images/seis_6.png'))
img.append(text_e(imgload[58]))
imgload.append(pygame.image.load('files/images/sete_7.png'))
img.append(text_e(imgload[59]))
imgload.append(pygame.image.load('files/images/oito_8.png'))
img.append(text_e(imgload[60]))
imgload.append(pygame.image.load('files/images/nove_9.png'))
img.append(text_e(imgload[61]))
imgload.append(pygame.image.load('files/images/zero_0.png'))
img.append(text_e(imgload[62]))
imgload.append(pygame.image.load('files/images/game over.png'))
img.append(text_e(imgload[63]))
imgload.append(pygame.image.load('files/images/loli_parte3.png'))
img.append(text_e(imgload[64]))
imgload.append(pygame.image.load('files/images/loli_parte3_2.png'))
img.append(text_e(imgload[65]))
imgload.append(pygame.image.load('files/images/loli_parte3_3.png'))
img.append(text_e(imgload[66]))
imgload.append(pygame.image.load('files/images/loli_parte3_4.png'))
img.append(text_e(imgload[67]))
imgload.append(pygame.image.load('files/images/ceu_lua.png'))
img.append(text_e(imgload[68]))
imgload.append(pygame.image.load('files/images/parede.jpg'))
img.append(text_e(imgload[69]))
imgload.append(pygame.image.load('files/images/tiro.png'))
img.append(text_e(imgload[70]))
imgload.append(pygame.image.load('files/images/policial_game.png'))
img.append(text_e(imgload[71]))
imgload.append(pygame.image.load('files/images/Edge.png'))
img.append(text_e(imgload[72]))
imgload.append(pygame.image.load('files/images/ataque1.png'))
img.append(text_e(imgload[73]))
imgload.append(pygame.image.load('files/images/ataque2.png'))
img.append(text_e(imgload[74]))
imgload.append(pygame.image.load('files/images/ataque3.png'))
img.append(text_e(imgload[75]))
imgload.append(pygame.image.load('files/images/sword.png'))
img.append(text_e(imgload[76]))

glutInit()
pts = 0
AUX = 0
vermelho = False
azul = False
verde = False
x = 0
y = 0
s = 0
C = 0
s2 = 100
HP = 0
nomeJogador = ''
game_over = False
multiplicador_pts1 = 1
multiplicador_pts2 = 1
qtde_lolis_capturadas = 0
aux_tempo_alternacao1 = 0
aux_back = False
aux_rand_ninja = 0
aux_t_col = 0
aux_t_ninjas = 0
VT = 0
n_colisoes_3 = 0
alterna_loli = True
ultima_tecla = 0
start = time.time()
esta_pausado = False
esta_querendo_confirmar = False
estou_em_transicao = False
parte = 'tela_inicial'
cont_fora_da_tela = 0
quadrado = {
    'id_text': 0,
    'id': 0,  # int
    'x': 0,  # float
    'y': 0,  # float
    'largura': 0,  # float
    'altura': 0,  # float
    'visivel': True,  # booleano
    'velocidade': 0,  # float/int
    'area': 0,  # float
    'n_colisoes': 0,
    'direcao': True,
    'direcaoY': True,
    'cor': (0, 0, 0),
    'tempo_resp': 5,
    'tempo_morte': 0
}
# Definição de um botão interativo
interavel = quadrado.copy()
interavel['x'] = 150  # desenhar o mouse inicialmente fora da tela
interavel['cor'] = (1, 0, 0)

# Definindo um objeto para seguir o mouse
seguidor_mouse = quadrado.copy()
seguidor_mouse['cor'] = (0, 0, 1)
seguidor_mouse['largura'] = 7
seguidor_mouse['altura'] = 7

# Definindo um quadrado para as telas
tela_inicial = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'id': 56, 'cor': (0, 0, 0)}
tela_creditos = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'id': 56, 'cor': (0, 0, 1)}
tela_instrucoes = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'id': 56, 'cor': (1, 0, 1)}
tela_ranking = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'id': 56, 'cor': (0, 1, 0)}

# Definição de fundos
backg = {'x': 0, 'y': 0, 'altura': 200, 'largura': 200, 'cor': [1, 1, 1], 'id': 30}
backg2 = {'x': 0, 'y': 100, 'altura': 400, 'largura': 200, 'cor': [1, 1, 1], 'id': 30}

# Definindo o meu anzol
anzol = quadrado.copy()
anzol['x'] = 20
anzol['y'] = 90
anzol['altura'] = 8
anzol['visivel'] = True
anzol['largura'] = 8
anzol['velocidade'] = 8
anzol['area'] = anzol['altura'] ** 2
anzol['cor'] = (1, 1, 1)
anzol['id'] = 'anzol'

# Definição de botões

# Definição do botão que inicializa o jogo
botao_iniciar_jogo = quadrado.copy()
botao_iniciar_jogo['id'] = 'btnInicializador'
botao_iniciar_jogo['x'] = 0
botao_iniciar_jogo['y'] = 0
botao_iniciar_jogo['largura'] = 60
botao_iniciar_jogo['altura'] = 25
botao_iniciar_jogo['cor'] = (0, 1, 1)

# Definição de um botão que vai para a tela de créditos
botao_creditos = botao_iniciar_jogo.copy()
botao_creditos['id'] = 'btnCreditos'
botao_creditos['x'] = -70
botao_creditos['y'] = 0

# Definição de um botão que vai acessa o ranking
botao_ranking = botao_iniciar_jogo.copy()
botao_ranking['id'] = 'btnRanking'
botao_ranking['x'] = 70
botao_ranking['y'] = 0

# Definição de um botão que vai sair do jogo
botao_sair = botao_iniciar_jogo.copy()
botao_sair['id'] = 'btnSair'
botao_sair['x'] = 0
botao_sair['y'] = -60

# Definição de um botão de instruções
botao_instrucoes = botao_iniciar_jogo.copy()
botao_instrucoes['id'] = 'btnInstrucoes'
botao_instrucoes['x'] = 0
botao_instrucoes['y'] = 60

# Definição de um botão para a borda
botao_borda = botao_iniciar_jogo.copy()
botao_borda['id'] = 'btnInstrucoes'
botao_borda['x'] = 0
botao_borda['y'] = 0

tela_i = quadrado.copy()
tela_i['altura'] = 200
tela_i['largura'] = 200
tela_i['cor'] = list(tela_i['cor'])
tela_i['cor'] = [0, 0, 0]

# Definição do botão de game over
game_over = quadrado.copy()
game_over['altura'] = 200
game_over['largura'] = 200
game_over['cor'] = (1, 0, 0)

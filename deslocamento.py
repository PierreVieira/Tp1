from objetos_primeira_parte import *
from random import randint
import gerador_de_coordenadas1
import globais
from math import cos, sin, pi
from OpenGL.GL import *
from time import time

def checkY(c):
    if all1[c]['y'] >= 110:
        globais.cont_fora_da_tela += 1
        all1[c]['visivel'] = True
        x_object = randint(-95, 95)
        y_object = randint(-95, -90)
        while gerador_de_coordenadas1.analise_de_proximidade(x_object, y_object, all1):
            y_object = randint(-110, -101)
            x_object = randint(-95, 95)
        all1[c]['x'] = x_object
        all1[c]['y'] = y_object

def deslocamento_0(c):
    t = 0
    t += all1[c]['velocidade'] / randint(200, 600)
    all1[c]['y'] += t
    checkY(c)

def deslocamento_1(c):
    t = all1[c]['velocidade'] / randint(400, 1200)
    all1[c]['y'] += t*1.73

    if all1[c]['x'] >= 95:
        all1[c]['direcao'] = False

    elif all1[c]['x'] <= -95:
        all1[c]['direcao'] = True

    if all1[c]['direcao']:
        all1[c]['x'] += t
    else:
        all1[c]['x'] -= t
    checkY(c)

def deslocamento_2(c):
    t = all1[c]['velocidade'] / randint(400, 1200)
    globais.soma_d2 += t
    all1[c]['y'] = all1[c]['x']**2 + globais.soma_d2
    if int(time() - globais.start) % 2 == 0:
        globais.direcao2 = True
    else:
        globais.direcao2 = False

    if globais.direcao2:
        all1[c]['x'] += 0.1*pi/10
    else:
        all1[c]['x'] -= 0.1*pi/10
    checkY(c)

def deslocar():
    for c in range(len(all1)):
        if all1[c]['id'] == 0:
            deslocamento_0(c)
        elif all1[c]['id'] == 1:
            deslocamento_1(c)
        elif all1[c]['id'] == 2:
            deslocamento_2(c)
        if (globais.cont_fora_da_tela+1) % 5 == 0 and globais.cont_fora_da_tela <= 20:
            all1[0+(globais.cont_fora_da_tela//5)]['id'] = 1
            all1[0+(globais.cont_fora_da_tela//5)]['cor'] = (1, 0, 1)
        #
        # elif (globais.cont_fora_da_tela+1) % 5 == 0 and 20 <= globais.cont_fora_da_tela <= 40:
        #     all1[4 + (globais.cont_fora_da_tela // 5)]['id'] = 2
        #     all1[4 + (globais.cont_fora_da_tela // 5)]['cor'] = (0, 0, 0)


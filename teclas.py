import globais
from OpenGL.GLUT import *
from time import time
from menu_pause import *
import menu_pause

def tecla(key, x = 0, y = 0):
    tec = ord(key)
    if tec == 27: #ESC
        end = time()
        print(end - globais.start)
        exit()
    elif tec == 114: #r
        print('reiniciando o programa')
    elif tec == 112 or tec == 80: #p
        globais.esta_pausado = not(globais.esta_pausado)
        print('Pausando o programa')
    elif tec == 97: #esquerda (a)
        globais.anzol['x'] -= globais.anzol['velocidade']
    elif tec == 100: #direita (d)
        globais.anzol['x'] += globais.anzol['velocidade']


def movimenta_anzol(self, key, x = 0, y = 0):
    if not(globais.esta_pausado):
        if self == GLUT_KEY_UP and globais.anzol['y'] <= 90:
            globais.anzol['y'] += globais.anzol['velocidade']
        elif self == GLUT_KEY_DOWN and globais.anzol['y'] >= -90:
            globais.anzol['y'] -= globais.anzol['velocidade']
        elif self == GLUT_KEY_LEFT and globais.anzol['x'] >= -90: #seta esquerda
            globais.anzol['x'] -= globais.anzol['velocidade']
        elif self == GLUT_KEY_RIGHT and globais.anzol['x'] <= 90: #seta direita
            globais.anzol['x'] += globais.anzol['velocidade']
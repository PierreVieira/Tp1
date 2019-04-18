from random import randint
from globais import *
def analise_de_proximidade(x_object, y_object, lista_objetos):
    for c in lista_objetos:
        distancia = ((x_object - c['x'])**2 + (y_object - c['y'])**2)**0.5
        if distancia < distancia_permitida:
            return True
    return False

def gerador_objetos2(lista_peixes, lista_traps):
    todos_objetos = []
    all_objects = []
    objeto = quadrado.copy()
    for c in lista_peixes:
        for d in c:
            todos_objetos.append(d)
    for c in lista_traps:
        for d in c:
            todos_objetos.append(d)
    for c in todos_objetos:
        x_object = randint(-95, 95)
        y_object = randint(-95, -20)
        while analise_de_proximidade(x_object, y_object, todos_objetos):
            x_object = randint(-95, 95)
            y_object = randint(-95, -65)
        # Definindo a lista de objetos
        c['x'] = x_object
        c['y'] = y_object
        all_objects.append(c)
    return all_objects
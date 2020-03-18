#-*- coding: utf-8 -*-

from pprint import pprint
from random import randint
from os import system
import time

FIL = 20
COL = 20

MUNDO = [[0] * FIL for x in xrange(COL)]

def soplar_vida():
    """ Creo celulas de vida en el mundo """
    for x in xrange(FIL):
        for y in xrange(COL):
            MUNDO[x][y] = randint(0,1)
  
def posicion_vida(f, c):
    """ Establezo la posicion en la 
        que se encuentra el explorador de vida, para establecer
        si se deja vivir o se mata la celula.
    """
    if (f == 0) and (c==0):
        vive_o_muere_celula(explorar_NORTE_OESTE(f, c), f, c)
    elif(f == (FIL-1)) and (c==0):
        vive_o_muere_celula(explorar_SUR_OESTE(f, c), f, c)
    elif (f == 0) and ( c == (COL-1)):
        vive_o_muere_celula(explorar_NORTE_ESTE(f, c), f, c)
    elif (f==(FIL-1)) and (c==(COL-1)):
        vive_o_muere_celula(explorar_SUR_ESTE(f, c), f, c)
    elif (f > 0 and f < (FIL-1)) and c == 0:
        vive_o_muere_celula(explorar_OESTE(f, c), f, c)
    elif f == 0 and (c > 0 and c < (COL-1)):
        vive_o_muere_celula(explorar_NORTE(f, c), f, c)
    elif (f > 0 and f < (FIL-1)) and c == (COL-1):
        vive_o_muere_celula(explorar_ESTE(f, c), f, c)
    elif(c > 0 and c < (COL-1)) and f == (FIL-1):
        vive_o_muere_celula(explorar_SUR(f, c), f, c)
    elif(f > 0 and f < (FIL-1)) and (c > 0 and c < (COL-1)):
        vive_o_muere_celula(explorar_centro_de_la_tierra(f, c), f, c)


def explorar_NORTE_OESTE(f, c):
    """ Explora la fila 0 columna 0 de la matriz MUNDO """
    celulas = []
    celulas.append(MUNDO[f][c+1])
    celulas.append(MUNDO[f+1][c+1])
    celulas.append(MUNDO[f+1][c])
    return celulas

def explorar_SUR_OESTE(f, c):
    """ Exploro la fila FIL y columna 0 de la matriz MUNDO """
    celulas = []
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c+1])
    celulas.append(MUNDO[f][c+1])
    return celulas

def explorar_NORTE_ESTE(f, c):
    """ Exploro la fila 0 columna COL de la matriz MUNDO"""
    celulas = []
    celulas.append(MUNDO[f][c-1])
    celulas.append(MUNDO[f+1][c-1])
    celulas.append(MUNDO[f+1][c])
    return celulas
    
def explorar_SUR_ESTE(f, c):
    """ Exploro la fila FIL y columna COL de la matriz MUNDO """
    celulas = []
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c-1])
    celulas.append(MUNDO[f][c-1])
    return celulas


def explorar_centro_de_la_tierra(f, c):
    """ Exploro el centro de la tierra """
    celulas = []
    celulas.append(MUNDO[f-1][c-1])
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c+1])
    celulas.append(MUNDO[f][c+1])
    celulas.append(MUNDO[f+1][c+1])
    celulas.append(MUNDO[f+1][c])
    celulas.append(MUNDO[f+1][c-1])
    celulas.append(MUNDO[f][c-1])
    return celulas

def explorar_OESTE(f, c):
    """ Exploro la columna 0 de la matriz mundo"""
    celulas = []
    
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c+1])
    celulas.append(MUNDO[f][c+1])
    celulas.append(MUNDO[f+1][c+1])
    celulas.append(MUNDO[f+1][c])
    return celulas

def explorar_NORTE(f, c):
    """Exploro la fila 0 de la matriz mundo """
    celulas = []
    celulas.append(MUNDO[f][c+1])
    celulas.append(MUNDO[f+1][c+1])
    celulas.append(MUNDO[f+1][c])
    celulas.append(MUNDO[f+1][c-1])
    celulas.append(MUNDO[f][c-1])
    return celulas

def explorar_ESTE(f, c):
    """ Exploro la columna COL de la matriz mundo"""
    celulas = []
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c-1])
    celulas.append(MUNDO[f][c-1])
    celulas.append(MUNDO[f+1][c-1])
    celulas.append(MUNDO[f+1][c])
    return celulas

def explorar_SUR(f, c):
    """ Exploro la fila FIL de la matriz mundo"""
    celulas = []
    celulas.append(MUNDO[f][c-1])
    celulas.append(MUNDO[f-1][c-1])
    celulas.append(MUNDO[f-1][c])
    celulas.append(MUNDO[f-1][c+1])
    celulas.append(MUNDO[f][c+1])
    return celulas
    
def vive_o_muere_celula(poblacion, f, c):
    """ Establezco vida o muerte segun el estado 
        de las celulas que rodean la celula actual, (le indico
        al explorador de vida que debe hacer, si matar o dejar vivir)
    """
    if poblacion.count(1) < 2:
        MUNDO[f][c] = 0
    elif poblacion.count(1) > 3:
        MUNDO[f][c] = 0
    elif poblacion.count(1) == 3:
        MUNDO[f][c] = 1


def verMundo():
    for x in xrange(FIL):
        for y in xrange(COL):
            if MUNDO[x][y] == 1:
                print chr(27)+"[32m"+"1",
            else:
                print chr(27)+"[2;30m"+"0",
                
        print '\n'



soplar_vida()
def main():
    """ Inicializa el juego de la vida """
    verMundo()
    for x in xrange(FIL):
        for y in xrange(COL):
            posicion_vida(x, y)
    system('clear')        
    verMundo()

# Creo mundos para ver los patrones de celulas            
for x in range(50):
    main()
    time.sleep(3)

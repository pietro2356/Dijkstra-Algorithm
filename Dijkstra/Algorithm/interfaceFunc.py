import math
grafo = {}
costoNodi = {}
parents = {}


def createNewNodo(nomeNodo):
    if type(nomeNodo) != 'str':
        grafo[nomeNodo] = {}
    else:
        return ValueError


def setLink(nodoStart, nodoEnd, peso):
    grafo[nodoStart][nodoEnd] = peso
    #if type(nodoStart) != 'str' and type(nodoEnd) != 'str' and type(peso) != 'int':

    #else:
    #    return ValueError


def setCostoNodi():
    for i in grafo.keys():
        costoNodi[i]


def outNodi():
    return grafo


def setParents():
    return Exception

import math

grafo = {}


def setNodo(nomeNodo):
    grafo[nomeNodo] = {}


def setNodoStart(nomeNodo):
    return ValueError


def setNodoEnd(nomeNodo):
    return ValueError

def setLink(nodoStart, nodoEnd, peso):
    grafo[nodoStart][nodoEnd] = peso


def setCostoNodi():
    return ValueError


def setParents():
    return ValueError
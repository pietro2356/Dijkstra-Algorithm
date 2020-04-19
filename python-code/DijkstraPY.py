import math

# Implementazione del grafo
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 6
grafo["start"]["b"] = 2

grafo["a"] = {}
grafo["a"]["end"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["end"] = 5

grafo["end"] = {}

# Tabella costi
costo_nodi = {}
costo_nodi["a"] = 6
costo_nodi["b"] = 2
costo_nodi["end"] = math.inf

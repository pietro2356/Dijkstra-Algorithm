import math
# Percorso:  START -> B -> C -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 2
grafo["start"]["c"] = 4

grafo["a"] = {}
grafo["a"]["d"] = 8

grafo["b"] = {}
grafo["b"]["c"] = 1
grafo["b"]["end"] = 7

grafo["c"] = {}
grafo["c"]["end"] = 1

grafo["d"] = {}
grafo["d"]["end"] = 2

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = 2
costoNodi["c"] = 4
costoNodi["d"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["d"] = None
parents["end"] = None

processati = []
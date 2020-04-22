import math
# Percorso:  START -> B -> A -> D -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 5

grafo["a"] = {}
grafo["a"]["c"] = 9
grafo["a"]["d"] = 4

grafo["b"] = {}
grafo["b"]["a"] = 1
grafo["b"]["d"] = 7

grafo["c"] = {}
grafo["c"]["end"] = 5

grafo["d"] = {}
grafo["d"]["c"] = 5
grafo["d"]["end"] = 3

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 8
costoNodi["b"] = 5
costoNodi["c"] = math.inf
costoNodi["d"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["end"] = None

processati = []
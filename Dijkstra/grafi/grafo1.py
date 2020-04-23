import math
# Percorso:  START -> A -> C -> D -> E -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["d"] = 8

grafo["a"] = {}
grafo["a"]["c"] = 2
grafo["a"]["b"] = 6

grafo["b"] = {}
grafo["b"]["end"] = 5

grafo["c"] = {}
grafo["c"]["d"] = 2
grafo["c"]["e"] = 9

grafo["d"] = {}
grafo["d"]["e"] = 3

grafo["e"] = {}
grafo["e"]["end"] = 1

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = math.inf
costoNodi["c"] = math.inf
costoNodi["d"] = 8
costoNodi["e"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["d"] = "start"
parents["e"] = None
parents["end"] = None

processati = []
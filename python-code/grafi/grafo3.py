import math
# Percorso:  START -> B -> D -> E -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 4
grafo["start"]["b"] = 2

grafo["a"] = {}
grafo["a"]["c"] = 10
grafo["a"]["d"] = 8

grafo["b"] = {}
grafo["b"]["d"] = 7
grafo["b"]["e"] = 10

grafo["c"] = {}
grafo["c"]["end"] = 2

grafo["d"] = {}
grafo["d"]["e"] = 1

grafo["e"] = {}
grafo["e"]["end"] = 4

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 4
costoNodi["b"] = 2
costoNodi["c"] = math.inf
costoNodi["d"] = math.inf
costoNodi["e"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["e"] = None
parents["end"] = None

processati = []
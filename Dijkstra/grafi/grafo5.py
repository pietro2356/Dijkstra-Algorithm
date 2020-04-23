import math
# Percorso:  START -> A -> C -> E -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 7

grafo["a"] = {}
grafo["a"]["c"] = 5

grafo["b"] = {}
grafo["b"]["c"] = 2

grafo["c"] = {}
grafo["c"]["d"] = 14
grafo["c"]["e"] = 2
grafo["c"]["end"] = 10

grafo["d"] = {}
grafo["d"]["end"] = 8

grafo["e"] = {}
grafo["e"]["end"] = 0

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = 7
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
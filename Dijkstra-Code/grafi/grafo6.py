import math
# Percorso:  START -> A -> C -> D -> E -> END
# OK

grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 20
grafo["start"]["c"] = 10

grafo["a"] = {}
grafo["a"]["d"] = 4

grafo["b"] = {}
grafo["b"]["a"] = 0
grafo["b"]["d"] = 5
grafo["b"]["e"] = 4

grafo["c"] = {}
grafo["c"]["e"] = 2
grafo["c"]["f"] = 1

grafo["d"] = {}
grafo["d"]["i"] = 40
grafo["d"]["h"] = 20
grafo["d"]["e"] = 2

grafo["e"] = {}
grafo["e"]["l"] = 5
grafo["e"]["g"] = 1

grafo["f"] = {}
grafo["f"]["e"] = 8

grafo["g"] = {}
grafo["g"]["l"] = 5

grafo["h"] = {}
grafo["h"]["l"] = 1
grafo["h"]["k"] = 20

grafo["i"] = {}
grafo["i"]["j"] = 1

grafo["j"] = {}
grafo["j"]["m"] = 7
grafo["j"]["k"] = 14

grafo["k"] = {}
grafo["k"]["n"] = 7

grafo["l"] = {}
grafo["l"]["o"] = 2
grafo["l"]["end"] = 8

grafo["m"] = {}
grafo["m"]["n"] = 0

grafo["n"] = {}
grafo["n"]["end"] = 1

grafo["o"] = {}
grafo["o"]["end"] = 2

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = 20
costoNodi["c"] = 10
costoNodi["d"] = math.inf
costoNodi["e"] = math.inf
costoNodi["f"] = math.inf
costoNodi["g"] = math.inf
costoNodi["h"] = math.inf
costoNodi["i"] = math.inf
costoNodi["j"] = math.inf
costoNodi["k"] = math.inf
costoNodi["l"] = math.inf
costoNodi["m"] = math.inf
costoNodi["n"] = math.inf
costoNodi["o"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["d"] = None
parents["e"] = None
parents["f"] = None
parents["g"] = None
parents["h"] = None
parents["i"] = None
parents["j"] = None
parents["k"] = None
parents["l"] = None
parents["m"] = None
parents["n"] = None
parents["o"] = None
parents["end"] = None

processati = []
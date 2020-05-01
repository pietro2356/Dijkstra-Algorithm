import math

grafo = {}
grafo["A"] = {}
grafo["A"]["B"] = 4
grafo["A"]["C"] = 2

grafo["B"] = {}
grafo["B"]["D"] = 7
grafo["B"]["C"] = 8

grafo["C"] = {}
grafo["C"]["D"] = 5
grafo["C"]["E"] = 2

grafo["D"] = {}
grafo["D"]["E"] = 20

grafo["E"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["A"] = 0
costoNodi["B"] = 4
costoNodi["C"] = 2
costoNodi["D"] = math.inf
costoNodi["E"] = math.inf


# Tabella parents:
parents = {}
parents["B"] = "A"
parents["C"] = "A"
parents["D"] = None
parents["E"] = None

processati = []

print("GRAFO:", grafo)
print("COSTO NODI:", costoNodi)
print("PARENTS:", parents)
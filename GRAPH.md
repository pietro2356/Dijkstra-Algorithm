# GUIDA ALLA CREAZIONE DEI GRAFI

#### IMMAGINE DEL GRAFO
![grafoStart](/img/grafoStart.png)

> **CREARE IL GRAFO PRINCIPALE**
```python
grafo = {}
```

> **CREARE I VARI NODI ED I LINK**
* I nodi saranno: start, a, b, c, d, e, end.
* Per prima cosa si creano i nodi senza alcun riferimento.
* Dopo verranno impostati i vari link tra i vari nodi:

```python
grafo["nome_nodo"] = {}
grafo["nome_nodo"]["nodo_arrivo"] = peso

# Link del nodo "start" al nodo A e D
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["d"] = 8

# Link del nodo "A" al nodo C e B
grafo["a"] = {}
grafo["a"]["c"] = 2
grafo["a"]["b"] = 6

# Link del nodo "B" al nodo END
grafo["b"] = {}
grafo["b"]["end"] = 5

# Link del nodo "C" al nodo D e E
grafo["c"] = {}
grafo["c"]["d"] = 2
grafo["c"]["e"] = 9

# Link del nodo "D" al nodo E
grafo["d"] = {}
grafo["d"]["e"] = 3

# Link del nodo "E" al nodo END
grafo["e"] = {}
grafo["e"]["end"] = 1

# L'ultimo nodo va lasciato senza link!
grafo["end"] = {}
```

> **IMPOSTAZIONE COSTO DEI NODI**
* Adesso dobbiamo creare un dizionario che tenga conto del peso di ogni singolo nodo
    * I nodi direttamente collegati al nodo di partenza avranno in automatico il peso del link.
    * I nodi non direttamente collegati al nodo di partenza avranno come valore temporaneo: infinito.
    * **IN QUESTO DIZIONARIO NON VA INDICATO IL NODO DI PARTENZA**

* si consigli di usare `math.inf` per il valore infinito utilizzabile importando il modulo *math* con: `import math`.

* Creiamo il dizionario:
```python   
costoNodi = {}
```
* Settiamo il dizionario:
```python
costoNodi["nodo"] = peso

costoNodi["a"] = 2
costoNodi["b"] = math.inf
costoNodi["c"] = math.inf
costoNodi["d"] = 8
costoNodi["e"] = math.inf
costoNodi["end"] = math.inf
```

> **CREAZIONE TABELLA DEI 'PARENTI'**
* Il dizionario che andiamo a creare adesso, serve per tenere traccia del percorso minimo da seguire prodotto dall'algoritmo.
    * Se il nodo non è direttamente collegato al nodo di partenza impostare come valore `None`.
    * È più semplice spiegare direttamente il codice. :wink:
    * **IN QUESTO DIZIONARIO NON VA INDICATO IL NODO DI PARTENZA**
    
* Creiamo il dizionario:
```python
parents = {}
```

* Settiamo il dizionario:
```python
# Se il nodo è direttamente collegato al nodo di partenza:
parents["nodo"] = "nodo_di_partenza"

# Se il nodo NON è direttamente collegato al nodo di partenza:
parents["nodo"] = None

# Quindi:
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["d"] = "start"
parents["e"] = None
parents["end"] = None
```

> **TABELLA DEI NODI PROCESSATI**
* Serve al prigramma per ricordare quali nodi ha già elaborato ed evitare che entri in loop.
```python
processati = []
```

### ULTIME COSE
* Adesso abbiamo finito, se tutto è adato bene il risualtato del programma dovrebbe essere questo:
```
Percorso:  START -> A -> C -> D -> E -> END
```
![grafoResult](/img/grafoResult.png)

### ESEMPI
* **Se vuoi vedere degli esempi, li puoi trovare dentro i file chiamati: `grafoN.py`.**
* **Per provarli non ti basta che copiare il codice al loro interno ed inserirlo nel file `Dijkstra.py` nell'apposita sezione.**


### RINGRAZIAMENTI

* **Sempre i notri poveri neuroni.**
* **La guida al markdown** - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)


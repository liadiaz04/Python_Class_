from collections import deque

def bfs_todos_caminos(laberinto, inicio, meta):
    filas, columnas = len(laberinto), len(laberinto[0])
    cola = deque([(inicio, [inicio])])
    todos_caminos = []
    
    while cola:
        (i, j), camino = cola.popleft()
        
        if (i, j) == meta:
            todos_caminos.append(camino)
            continue
        
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in direcciones:
            ni, nj = i + di, j + dj
            if 0 <= ni < filas and 0 <= nj < columnas and laberinto[ni][nj] == 0 and (ni, nj) not in camino:
                cola.append(((ni, nj), camino + [(ni, nj)]))
    
    return todos_caminos

# Ejemplo de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
entrada = (0, 0)
salida = (4, 4)

caminos = bfs_todos_caminos(laberinto, entrada, salida)
for camino in caminos:
    print(camino)

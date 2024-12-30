# Prioritätswarteschlange
import heapq

def Dijkstra(graph, start):
    num_nodes = len(graph)

    dist = [float("inf")] * num_nodes
    prev = [None] * num_nodes
    dist[start] = 0
    
    # Prioritätswarteschlange mit Distanz und Knoten
    Q = [(0, start)]

    while Q:
        # Node mit minimaler Distanz entfernen
        current_dist, u = heapq.heappop(Q)

        if current_dist > dist[u]:
            continue
        
        # Nachbarn des aktuellen Nodes prüfen
        for v, weight in enumerate(graph[u]):
            if weight > 0:  # Wenn Kante zwischen u und v existiert
                alt = dist[u] + weight
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(Q, (alt, v))
    
    return dist, prev

graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 4, 2, 0],
    [4, 4, 0, 3, 1],
    [0, 2, 3, 0, 5],
    [0, 0, 1, 5, 0],
]

start = 0
dist, prev = Dijkstra(graph, start)
print("Distanzen:", dist) # Distanzen: [0, 1, 4, 3, 5]
print("Vorgänger:", prev) # Vorgänger: [None, 0, 0, 1, 2]
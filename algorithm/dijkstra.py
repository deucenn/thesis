# Prioritätswarteschlange & Runtimemessung
import heapq
import time

def Dijkstra(graph, start):
    num_nodes = len(graph)
    start_time = time.time()

    dist = [float("inf")] * num_nodes
    prev = [None] * num_nodes
    dist[start] = 0
    
    # Prioritätswarteschlange mit Distanz und Nodes
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

    end_time = time.time()

    elapsed = end_time - start_time
    
    return dist, prev, elapsed


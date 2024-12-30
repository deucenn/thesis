# Priotitätswarteschlange & Runtimetests
import heapq
import time

def AStar(graph, start, goal, heuristic):
    num_nodes = len(graph)
    start_time = time.time()

    # g-Werte (Kosten vom Startknoten zu jedem Knoten) und h-Werte (Heuristik)
    g = [float("inf")] * num_nodes
    h = [float("inf")] * num_nodes
    f = [float("inf")] * num_nodes
    prev = [None] * num_nodes
    
    g[start] = 0
    h[start] = heuristic[start]  # Heuristik für den Startknoten
    f[start] = g[start] + h[start]  # f-Wert für den Startknoten

    # Prioritätswarteschlange mit f-Werten und Knoten
    Q = [(f[start], start)]

    while Q:
        # Knoten mit minimalem f-Wert entfernen
        current_f, u = heapq.heappop(Q)

        # Wenn der Zielknoten erreicht ist
        if u == goal:
            break

        # Nachbarn des aktuellen Knotens prüfen
        for v, weight in enumerate(graph[u]):
            if weight > 0:  # Wenn Kante zwischen u und v existiert
                g_v = g[u] + weight
                h_v = heuristic[v]
                f_v = g_v + h_v

                if f_v < f[v]:
                    g[v] = g_v
                    h[v] = h_v
                    f[v] = f_v
                    prev[v] = u
                    heapq.heappush(Q, (f_v, v))

    end_time = time.time()

    elapsed = end_time - start_time
    
    return g, prev, elapsed

# Beispiel für die Heuristik (z.B. Manhattan-Distanz oder euklidische Distanz)
def example_heuristic(node):
    # Dummy-Implementierung: einfache Heuristik als Platzhalter
    return abs(node - goal)

# Beispielgraph (Adjazenzmatrix)
graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 2, 6, 0, 0],
    [4, 2, 0, 3, 5, 0],
    [0, 6, 3, 0, 2, 6],
    [0, 0, 5, 2, 0, 4],
    [0, 0, 0, 6, 4, 0]
]

start = 0  # Startknoten
goal = 5   # Zielknoten
heuristic = [10, 9, 7, 5, 3, 0]  # Dummy-Heuristikwerte (z.B. euklidische oder Manhattan-Distanz)

g, prev, elapsed = AStar(graph, start, goal, heuristic)

print(f"Distanz: {g}")
print(f"Vorgänger: {prev}")
print(f"Laufzeit: {elapsed} Sekunden\n")

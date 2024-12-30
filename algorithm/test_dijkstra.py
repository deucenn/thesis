from dijkstra import Dijkstra
import random

# Tests mit großen Datensätzen
def generate_large_graph(num_nodes, max_weight=100):
    """
    Generiert einen zufälligen dichten Graphen mit `num_nodes` Knoten.
    Jede Kante ist zufällig gewichtet.
    """
    graph = [[0 if i == j else random.randint(1, max_weight) if random.random() < 0.3 else 0
              for j in range(num_nodes)] for i in range(num_nodes)]
    return graph

def test_dijkstra_with_runtime():
    num_nodes = 1000  # Anzahl der Knoten
    graph = generate_large_graph(num_nodes)
    start_node = 0

    print(f"Test mit {num_nodes} Knoten gestartet.")
    dist, prev, elapsed = Dijkstra(graph, start_node)
    print(f"Algorithmus abgeschlossen. Laufzeit: {elapsed:.4f} Sekunden")
    print("Kürzeste Distanz zu den ersten 10 Knoten:", dist[:10])
    print("Vorgänger der ersten 10 Knoten:", prev[:10])
    print("-" * 50)

if __name__ == "__main__":
    test_dijkstra_with_runtime()

# Tests mit kleinen Datensätzen
def print_results(graph, start):
    dist, prev, elapsed = Dijkstra(graph, start)
    print(f"Startknoten: {start}")
    print(f"Distanzen: {dist}")
    print(f"Vorgänger: {prev}")
    print(f"Runtime: {elapsed} seconds")
    print("-" * 50)


if __name__ == "__main__":
    print("Test 1: Einfacher Graph mit längeren Wegen")
    graph1 = [
        [0, 1, 4, 0, 0],
        [1, 0, 4, 2, 0],
        [4, 4, 0, 3, 1],
        [0, 2, 3, 0, 5],
        [0, 0, 1, 5, 0],
    ]
    print_results(graph1, 0)

    print("Test 2: Größerer Graph mit langen Verbindungen")
    graph2 = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0],
    ]
    print_results(graph2, 0)

    print("Test 3: Disconnected Graph mit unerreichbaren Knoten")
    graph3 = [
        [0, 10, 0, 0, 0],
        [10, 0, 0, 0, 0],
        [0, 0, 0, 5, 0],
        [0, 0, 5, 0, 15],
        [0, 0, 0, 15, 0],
    ]
    print_results(graph3, 0)

    print("Test 4: Graph mit einer komplexen Struktur")
    graph4 = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    print_results(graph4, 1)

    print("Test 5: Graph mit sehr langen Wegen")
    graph5 = [
        [0, 100, 200, 0, 0],
        [100, 0, 150, 250, 0],
        [200, 150, 0, 100, 300],
        [0, 250, 100, 0, 50],
        [0, 0, 300, 50, 0],
    ]
    print_results(graph5, 0)


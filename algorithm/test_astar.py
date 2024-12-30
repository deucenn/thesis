from astar import AStar 
import random

# Zufällige Heuristikfunktion
def generate_heuristics(num_nodes):
    """
    Generiert eine zufällige Heuristik für jeden Knoten.
    """
    return [random.randint(1, 100) for _ in range(num_nodes)]

# Generiert einen zufälligen dichten Graphen
def generate_large_graph(num_nodes, max_weight=100):
    """
    Generiert einen zufälligen dichten Graphen mit `num_nodes` Knoten.
    Jede Kante ist zufällig gewichtet.
    """
    graph = [[0 if i == j else random.randint(1, max_weight) if random.random() < 0.3 else 0
              for j in range(num_nodes)] for i in range(num_nodes)]
    return graph

def test_astar_with_runtime():
    num_nodes = 1000  # Anzahl der Knoten
    graph = generate_large_graph(num_nodes)
    heuristic = generate_heuristics(num_nodes)  # Zufällige Heuristik für A*
    start_node = 0
    goal_node = num_nodes - 1  # Zielknoten ist der letzte Knoten

    print(f"Test mit {num_nodes} Knoten gestartet.")
    
    # A* Algorithmus ausführen
    dist, prev, elapsed = AStar(graph, start_node, goal_node, heuristic)
    
    print(f"A* Algorithmus abgeschlossen. Laufzeit: {elapsed:.4f} Sekunden")
    print("Kürzeste Distanz zum Zielknoten:", dist[goal_node])
    print("Vorgänger der ersten 10 Knoten:", prev[:10])
    print("-" * 50)

if __name__ == "__main__":
    test_astar_with_runtime()


def test_AStar():
    # Test 1: Einfacher Graph
    graph1 = [
        [0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ]
    heuristic1 = [5, 4, 3, 2, 1, 0]  # Beispiel für eine Heuristik (z.B. Distanz zum Zielknoten)
    start1 = 0
    goal1 = 5

    print("Test 1: Einfacher Graph")
    g1, prev1, elapsed1 = AStar(graph1, start1, goal1, heuristic1)
    print("Distanzen:", g1)
    print("Vorgänger:", prev1)
    print("Laufzeit:", elapsed1, "Sekunden\n")

    # Test 2: Ein Graph mit mehreren möglichen Wegen
    graph2 = [
        [0, 2, 0, 1, 0],
        [2, 0, 3, 0, 0],
        [0, 3, 0, 1, 5],
        [1, 0, 1, 0, 2],
        [0, 0, 5, 2, 0]
    ]
    heuristic2 = [7, 6, 5, 3, 0]  # Beispiel-Heuristikwerte
    start2 = 0
    goal2 = 4

    print("Test 2: Ein Graph mit mehreren möglichen Wegen")
    g2, prev2, elapsed2 = AStar(graph2, start2, goal2, heuristic2)
    print("Distanzen:", g2)
    print("Vorgänger:", prev2)
    print("Laufzeit:", elapsed2, "Sekunden\n")

    # Test 3: Einfacher Graph mit direkter Verbindung
    graph3 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    heuristic3 = [1, 0, 0]  # Einfaches Beispiel
    start3 = 0
    goal3 = 2

    print("Test 3: Einfacher Graph mit direkter Verbindung")
    g3, prev3, elapsed3 = AStar(graph3, start3, goal3, heuristic3)
    print("Distanzen:", g3)
    print("Vorgänger:", prev3)
    print("Laufzeit:", elapsed3, "Sekunden\n")

    # Test 4: Kein erreichbarer Zielknoten
    graph4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    heuristic4 = [1, 1, 0]  # Zielknoten ist nicht erreichbar
    start4 = 0
    goal4 = 2

    print("Test 4: Kein erreichbarer Zielknoten")
    g4, prev4, elapsed4 = AStar(graph4, start4, goal4, heuristic4)
    print("Distanzen:", g4)
    print("Vorgänger:", prev4)
    print("Laufzeit:", elapsed4, "Sekunden\n")

test_AStar()

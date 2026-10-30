# Iterative Deepening Depth-First Search (IDDFS)==-

graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'N': [],
    'M': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}


def dls(graph, node, goal, limit, path, visited_order):
    """Depth-Limited Search (DLS)"""
    visited_order.append(node)

   
    if node == goal:
        return True

    if limit <= 0:
        return False

   
    for neighbour in graph.get(node, []):
        path.append(neighbour)
        if dls(graph, neighbour, goal, limit - 1, path, visited_order):
            return True
        path.pop()  # Backtrack

    return False


def iddfs(graph, start, goal, max_depth):

    print(f"--- IDDFS Search: Starting from '{start}' to find '{goal}' ---\n")

    for depth in range(max_depth + 1):
        visited_order = []
        path = [start]

        print(f"Depth Limit = {depth}:")
        found = dls(graph, start, goal, depth, path, visited_order)

        print("  Nodes Visited:", " -> ".join(visited_order))

        if found:
            print(f"\n[Goal Found!]")
            print(f"Goal '{goal}' is reached at Depth: {depth}")
            print("Optimal Path:", " -> ".join(path))
            return True
        else:
            print("  Result: Goal not found at this limit.\n")

    print(f"Goal '{goal}' not found within maximum depth of {max_depth}.")
    return False


iddfs(graph, start="A", goal="G", max_depth=3)
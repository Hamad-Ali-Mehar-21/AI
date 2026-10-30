# Lab 5 - Task 2

# from collections import deque

# def bfs_search_goal(graph, start_node, goal_node):
   
#     # Track visited nodes
#     visited = set()
    
#     queue = deque([(start_node, [start_node])])
    
#     visited.add(start_node)
    
#     print(f"Starting BFS from '{start_node}' looking for '{goal_node}'...\n")
    
#     while queue:
#         # Pop the first element from our queue
#         current_node, path = queue.popleft()
#         print(f"Checking node: {current_node}")
        
#         # Did we find our goal?
#         if current_node == goal_node:
#             print(f"\nSuccess! Found goal node '{goal_node}'.")
#             print(f"Path to goal: {' -> '.join(path)}")
#             return True
            
#         # If not, let's look at its neighbors
        
#         for neighbor in graph.get(current_node, []):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 # Add neighbor to queue along with the updated path
#                 queue.append((neighbor, path + [neighbor]))
                
#     # If we exhaust the queue without finding the goal
#     print(f"\nGoal node '{goal_node}' was not found in the graph.")
#     return False

# if __name__ == "__main__":

    
#     tree_graph = {
#         'A': ['B', 'F', 'D', 'E'],
#         'B': ['K', 'J'],
#         'F': [],
#         'D': ['G'],
#         'E': ['C', 'H', 'I'],
#         'K': ['N', 'M'],
#         'J': [],
#         'G': [],
#         'C': [],
#         'H': [],
#         'I': ['L'],
#         'N': [],
#         'M': [],
#         'L': []
#     }
    
#     # Apply BFS to find 'G' starting from 'A'
#     bfs_search_goal(tree_graph, 'A', 'G')




def bfs_search_goal(graph, start_node, goal_node):

    visited = set()
    queue = [(start_node, [start_node])]

    visited.add(start_node)

    print(f"Starting BFS from '{start_node}' looking for '{goal_node}'...\n")

    while queue:
        current_node, path = queue.pop(0)

        print(f"Checking node: {current_node}")

        if current_node == goal_node:
            print(f"\nSuccess! Found goal node '{goal_node}'.")
            print(f"Path to goal: {' -> '.join(path)}")
            return True

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print(f"\nGoal node '{goal_node}' was not found in the graph.")
    return False


tree_graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}
bfs_search_goal(tree_graph, 'A', 'G')

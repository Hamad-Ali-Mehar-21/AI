

# Depth-First Search Using Stack

graph={
    'A': ['B','F','D','E'],
    'B': ['K','J'],
    'K': ['N','M'],
    'J':[],
    'N':[],
    'M':[],
    'F':[],
    'D':['G'],
    'G':[],
    'E':['C','H','I'],
    'C':[],
    'H':[],
    'I':['L'],
    'L':[]
}



def dfs(graph,start,goal):
    
    stack=[start]
    visited =[]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            print("Visited:",node)

            if node == goal:
                print("Goal Found:",goal)
                print("DFS Traversal:", "->".join(visited))
                return

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    print("Goal Not Found!")

dfs(graph,"A","Z")
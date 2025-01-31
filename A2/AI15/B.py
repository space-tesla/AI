#Q.2 Write a program to implement the Iterative Deepening Depth First 
#Search (IDDFS) algorithm. [Goal Node = G]


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

def depth_limited_search(graph, start, goal, depth):
    if start == goal:
        return True
    if depth <= 0:
        return False
    for neighbor in graph[start]:
        if depth_limited_search(graph, neighbor, goal, depth - 1):
            print(neighbor, end=" ")
            return True
    return False

def iterative_deepening_dfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth}:")
        if depth_limited_search(graph, start, goal, depth):
            print(start)
            return True
    return False

print("IDDFS traversal path to reach goal node 'G':")
iterative_deepening_dfs(graph, 'A', 'G', 3)


"""Output:

IDDFS traversal path to reach goal node 'G':
Searching at depth 0:
Searching at depth 1:
Searching at depth 2:
Searching at depth 3:
G C A

This output shows the path traced by Iterative Deepening DFS from the start node `A` to the goal node `G`.
"""



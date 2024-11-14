# Q.2) Write a Python program to implement Breadth First Search algorithm. Refer to the following graph as an input for the program. [Initial node=1, Goal node=8]

from collections import deque

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 8],
    7: [3, 8],
    8: [4, 5, 6, 7]
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    path = []

    while queue:
        node = queue.popleft()
        if node == goal:
            path.append(node)
            return path

        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return path

start_node = 1
goal_node = 8
path = bfs(graph, start_node, goal_node)
print("BFS traversal path to reach goal node 8:", path)


# Output:
#BFS traversal path to reach goal node 8: [1, 2, 3, 4, 5, 6, 7, 8]



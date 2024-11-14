
# Q.2 Write a Python program to implement the Heuristic Search algorithm.

class Node:
    def _init_(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.parent = None
        self.children = []

def add_child(node, child_node):
    node.children.append(child_node)
    child_node.parent = node

def heuristic_search(start_node, goal_node):
    open_list = [start_node]
    closed_list = []
    
    while open_list:
        open_list.sort(key=lambda x: x.heuristic)
        current_node = open_list.pop(0)
        
        print(f"Visiting node: {current_node.name}, Heuristic: {current_node.heuristic}")
        
        if current_node.name == goal_node.name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.reverse()
            return path
        
        closed_list.append(current_node)
        
        for child in current_node.children:
            if child not in open_list and child not in closed_list:
                open_list.append(child)
    
    return None

start = Node('A', 6)
goal = Node('F', 0)

B = Node('B', 4)
C = Node('C', 3)
D = Node('D', 1)
E = Node('E', 2)


add_child(start, B)
add_child(start, C)
add_child(B, D)
add_child(C, E)
add_child(D, goal)
add_child(E, goal)

path = heuristic_search(start, goal)

if path:
    print("Path to goal:", " -> ".join(path))
else:
    print("No path found")


Output:
Visiting node: A, Heuristic: 6
Visiting node: C, Heuristic: 3
Visiting node: E, Heuristic: 2
Visiting node: D, Heuristic: 1
Visiting node: F, Heuristic: 0
Path to goal: A -> C -> E -> F


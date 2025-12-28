import networkx as nx
from collections import deque

G = nx.Graph()

edges = [
    # Path 1: Short path (A -> M -> Z)
    ("Station A", "Station M"),
    ("Station M", "Station Z"),

    # Path 2: Long path (A -> B -> C -> D -> E -> Z)
    ("Station A", "Station B"),
    ("Station B", "Station C"),
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    ("Station E", "Station Z"),
    
    # Dead-end branch (just for graph complexity)
    ("Station B", "Station K_DeadEnd")
]

G.add_edges_from(edges)

def dfs_paths(graph, start, goal):
    """
    Finds paths using Depth-First Search.
    Uses a Stack (LIFO).
    """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()        
        neighbors = sorted(set(graph[vertex]) - set(path), reverse=True)
        
        for next_node in neighbors:
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))

def bfs_paths(graph, start, goal):
    """
    Finds paths using Breadth-First Search.
    Uses a Queue (FIFO).
    """
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        
        neighbors = set(graph[vertex]) - set(path)
        
        for next_node in neighbors:
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))


start_node = "Station A"
end_node = "Station Z"

dfs_result = list(dfs_paths(G, start_node, end_node))
bfs_result = list(bfs_paths(G, start_node, end_node))

print(f"--- Pathfinding from {start_node} to {end_node} ---\n")

print(f"BFS Path (Breadth-First): {bfs_result[0]}")
print(f"BFS Steps: {len(bfs_result[0]) - 1}")
print("-" * 40)

print(f"DFS Path (Depth-First):   {dfs_result[0]}")
print(f"DFS Steps: {len(dfs_result[0]) - 1}")

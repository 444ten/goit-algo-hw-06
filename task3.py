import networkx as nx
import heapq

G = nx.Graph()

weighted_edges = [
    ("Station A", "Station M", 10),
    ("Station M", "Station Z", 10),
    ("Station A", "Station B", 1),
    ("Station B", "Station C", 1),
    ("Station C", "Station D", 1),
    ("Station D", "Station E", 1),
    ("Station E", "Station Z", 1),
    ("Station B", "Station K", 5)
]

G.add_weighted_edges_from(weighted_edges)

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    predecessors = {node: None for node in graph.nodes()}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes.get('weight', 1) # Default weight is 1 if not specified
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.insert(0, current_node)
        if current_node == start:
            break
        current_node = predecessors[current_node]
    
    if path[0] == start:
        return path
    return []


print(f"{'Start':<10} | {'End':<10} | {'Time (min)':<10} | {'Path'}")
print("-" * 60)

nodes = list(G.nodes())

for start_node in nodes:
    distances, predecessors = dijkstra(G, start_node)
    
    for end_node in nodes:
        if start_node == end_node:
            continue
            
        path = reconstruct_path(predecessors, start_node, end_node)
        total_weight = distances[end_node]
        
        if total_weight != float('infinity'):
             print(f"{start_node:<10} | {end_node:<10} | {total_weight:<10} | {path}")

print("-" * 60)

dists, preds = dijkstra(G, "Station A")
final_path = reconstruct_path(preds, "Station A", "Station Z")
print(f"\nSpecific Check A -> Z: {final_path}, Time: {dists['Station Z']}")
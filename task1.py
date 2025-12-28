import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Metro
edges = [
    # Red Line (1)
    ("Station A", "Station B"),
    ("Station B", "Station C"), # Interchange
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    
    # Blue Line (2)
    ("Station F", "Station C"), # Intersection with Red Line at C
    ("Station C", "Station G"),
    ("Station G", "Station H"), # Interchange
    
    # Green Line (3)
    ("Station I", "Station B"), # Intersection with Red Line at B
    ("Station B", "Station J"),
    ("Station J", "Station H"), # Intersection with Blue Line at H
    ("Station H", "Station K")
]

G.add_edges_from(edges)

print(f"Number of nodes (stations): {G.number_of_nodes()}")
print(f"Number of edges (connections): {G.number_of_edges()}")

print("\nNode Degrees:")
for node, degree in G.degree():
    print(f"{node}: {degree}")

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42) # Layout for consistent positioning

nx.draw(G, pos, 
        with_labels=True, 
        node_color='skyblue', 
        node_size=2000, 
        edge_color='gray', 
        font_size=10, 
        font_weight='bold')

plt.title("City Metro Network Model")
plt.show()
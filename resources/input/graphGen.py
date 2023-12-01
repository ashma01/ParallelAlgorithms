import networkx as nx
import random

# Define the number of nodes for the graph
num_nodes = 2000
# Calculate the number of edges for a complete graph
num_edges = num_nodes * (num_nodes - 1) // 2

# Create a fully connected graph (complete graph)
G = nx.complete_graph(num_nodes)


# Generate unique weights for each edge
all_weights = random.sample(range(1, num_edges + 1), num_edges)

# Assign a unique weight to each edge
edge_weights = iter(all_weights)
for u, v in G.edges():
    G[u][v]['weight'] = next(edge_weights)


mst = nx.minimum_spanning_tree(G, weight='weight')
total_weight = sum(data['weight'] for u, v, data in mst.edges(data=True))

print("Total weight of MST:", total_weight)    

# Define the path for the output file
output_file_path = '/Users/ashmaparveen/Desktop/DesktopData/StudyMaterial/Fall23/ParallelAlgorithm/MavenProject/BenchMarkMST/src/main/resources/input/input_file.txt'
# Write the edges to a text file, with the number of nodes at the beginning
with open(output_file_path, 'w') as file:
    # First write the number of nodes
    file.write(f"{num_nodes}\n")
    # Then write all the edges with their weights
    for u, v, data in G.edges(data=True):
        file.write(f"{u} {v} {data['weight']}\n")

print(f"Graph with {num_nodes} nodes and fully connected edges with unique weights written to {output_file_path}")

import networkx as nx
import matplotlib.pyplot as plt
import math

# Create a directed graph
g = nx.DiGraph()

# Define the files and their dependencies
files = {
    "app.py": ["pipeline.py"],
    "pipeline.py": ["retriever.py", "generator.py", "preprocessor.py", "postprocessor.py", "config.py", "prompt_builder.py"],
    "retriever.py": ["embedding.py", "config.py"],
    "generator.py": ["config.py"],
    "preprocessor.py": [],
    "postprocessor.py": [],
    "embedding.py": ["config.py"],
    "data_loader.py": ["config.py", "utils.py"],
    "indexer.py": ["data_loader.py", "embedding.py"],
    "prompt_builder.py": ["utils.py", "constants.py"],
    "config.py": [],
    "utils.py": [],
    "constants.py": []
}

# Add edges to the graph based on dependencies
for file, dependencies in files.items():
    for dependency in dependencies:
        g.add_edge(dependency, file)

# Arrange nodes in a circular layout
nodes = list(g.nodes)
num_nodes = len(nodes)
angle_step = 2 * math.pi / num_nodes

pos = {
    node: (math.cos(i * angle_step), math.sin(i * angle_step))
    for i, node in enumerate(nodes)
}

# Draw the graph with circular layout
plt.figure(figsize=(14, 14))
nx.draw_networkx_nodes(g, pos, node_size=4000, node_color="lightblue")
nx.draw_networkx_edges(
    g, pos, arrowstyle="-|>", arrowsize=75, edge_color="black"
)
nx.draw_networkx_labels(g, pos, font_size=10, font_color="black")

plt.title("Workflow of RAG Project Structure (Circular Layout)", fontsize=16)
plt.axis("off")
plt.show()

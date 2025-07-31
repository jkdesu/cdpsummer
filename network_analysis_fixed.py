import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# Set up the figure with a larger size
plt.figure(figsize=(16, 12))
plt.style.use('default')

# Create a directed graph
G = nx.DiGraph()

# Define more nodes to create density (invisible stuff but influential)
nodes = {
    'Cultural_Trend': 'Cultural Trends',
    'Social_Media': 'Social Media Hype',
    'Economic_Factor': 'Economic Factors',
    'Consumer_Psychology': 'Consumer Psychology',
    'Brand_Value': 'Brand Value',
    'Scarcity_Logic': 'Artificial Scarcity',
    'Collector_Behavior': 'Collector Behavior',
    'Market_Dynamics': 'Market Dynamics',
    'Hype_Cycle': 'Hype Cycles',
    'Cultural_Capital': 'Cultural Capital',
    'Identity_Formation': 'Identity Formation',
    'Value_Construction': 'Value Construction',
    'Network_Effects': 'Network Effects',
    'Influence_Propagation': 'Influence Propagation',
    'Hidden_Structures': 'Hidden Structures',
    'Digital_Infrastructure': 'Digital Infrastructure',
    'Algorithmic_Bias': 'Algorithmic Bias',
    'Attention_Economy': 'Attention Economy',
    'FOMO_Psychology': 'FOMO Psychology',
    'Status_Signaling': 'Status Signaling',
    'Community_Formation': 'Community Formation',
    'Exclusivity_Logic': 'Exclusivity Logic',
    'Trend_Amplification': 'Trend Amplification',
    'Value_Perception': 'Value Perception',
    'Cultural_Reinforcement': 'Cultural Reinforcement',
    'Network_Cascades': 'Network Cascades',
    'Influence_Clusters': 'Influence Clusters',
    'Hidden_Hierarchies': 'Hidden Hierarchies',
    'Systemic_Biases': 'Systemic Biases',
    'Power_Dynamics': 'Power Dynamics',
    'Information_Flow': 'Information Flow',
    'Behavioral_Feedback': 'Behavioral Feedback',
    'Cultural_Contagion': 'Cultural Contagion'
}

# Add nodes to the graph
for node_id, node_label in nodes.items():
    G.add_node(node_id, label=node_label)

# Create a much denser network with guaranteed connections
edges = []

# Base connections (core relationships)
base_connections = [
    ('Cultural_Trend', 'Social_Media'),
    ('Social_Media', 'Consumer_Psychology'),
    ('Consumer_Psychology', 'Collector_Behavior'),
    ('Collector_Behavior', 'Market_Dynamics'),
    ('Market_Dynamics', 'Brand_Value'),
    ('Brand_Value', 'Scarcity_Logic'),
    ('Scarcity_Logic', 'Cultural_Trend'),
    ('Economic_Factor', 'Market_Dynamics'),
    ('Cultural_Capital', 'Identity_Formation'),
    ('Identity_Formation', 'Consumer_Psychology'),
    ('Value_Construction', 'Brand_Value'),
    ('Network_Effects', 'Influence_Propagation'),
    ('Influence_Propagation', 'Cultural_Trend'),
    ('Hidden_Structures', 'Network_Effects'),
    ('Hype_Cycle', 'Social_Media'),
    ('Social_Media', 'Hype_Cycle'),
    ('Cultural_Capital', 'Value_Construction'),
    ('Market_Dynamics', 'Economic_Factor'),
    ('Collector_Behavior', 'Cultural_Capital'),
    ('Scarcity_Logic', 'Network_Effects'),
    ('Hidden_Structures', 'Cultural_Trend'),
    ('Identity_Formation', 'Collector_Behavior'),
    ('Value_Construction', 'Economic_Factor'),
    ('Influence_Propagation', 'Consumer_Psychology')
]

# Add base connections
for u, v in base_connections:
    weight = np.random.uniform(0.6, 0.9)
    edges.append((u, v, {'weight': weight, 'label': 'Influences'}))

# Ensure every node has at least 2 connections
node_list = list(nodes.keys())
for node in node_list:
    # Find nodes that don't have enough connections
    in_degree = G.in_degree(node)
    out_degree = G.out_degree(node)
    total_degree = in_degree + out_degree
    
    if total_degree < 2:
        # Add connections to this node
        potential_targets = [n for n in node_list if n != node]
        for target in np.random.choice(potential_targets, min(2, len(potential_targets)), replace=False):
            if (node, target) not in [(e[0], e[1]) for e in edges]:
                weight = np.random.uniform(0.4, 0.8)
                edges.append((node, target, {'weight': weight, 'label': 'Affects'}))

# Add many more connections to create density
additional_nodes = list(nodes.keys())
for i in range(80):  # Add 80 more random connections
    u = np.random.choice(additional_nodes)
    v = np.random.choice(additional_nodes)
    if u != v and (u, v) not in [(e[0], e[1]) for e in edges]:
        weight = np.random.uniform(0.3, 0.8)
        edges.append((u, v, {'weight': weight, 'label': 'Affects'}))

# Add edges to the graph
for edge in edges:
    G.add_edge(edge[0], edge[1], **edge[2])

# Create the layout - using spring layout with higher k for more spread
pos = nx.spring_layout(G, k=2, iterations=100, seed=42)

# Create the plot
fig, ax = plt.subplots(figsize=(16, 12))

# Draw edges with clear color differences based on weight
edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
edge_widths = [1.5 + 3 * w for w in edge_weights]  # Thicker, more visible lines

# Create color-coded edges based on weight ranges
edge_colors = []
for weight in edge_weights:
    if weight > 0.8:
        edge_colors.append('#1f77b4')  # Blue for strong connections
    elif weight > 0.6:
        edge_colors.append('#ff7f0e')  # Orange for medium connections
    elif weight > 0.4:
        edge_colors.append('#2ca02c')  # Green for moderate connections
    else:
        edge_colors.append('#d62728')  # Red for weak connections

# Draw edges with distinct colors
nx.draw_networkx_edges(G, pos, 
                      edge_color=edge_colors,
                      alpha=0.8,  # Consistent opacity
                      width=edge_widths,
                      arrows=True,  # Add arrows to show direction
                      arrowsize=12,
                      arrowstyle='->',
                      connectionstyle='arc3,rad=0.1')  # More curved for clarity

# Draw nodes with varying sizes and colors based on centrality
node_sizes = [200 + 300 * nx.degree_centrality(G)[node] for node in G.nodes()]
node_colors = []
for node in G.nodes():
    in_degree = nx.in_degree_centrality(G)[node]
    out_degree = nx.out_degree_centrality(G)[node]
    if in_degree > 0.15:  # Highly influenced
        node_colors.append('#ff6b6b')  # Red
    elif out_degree > 0.15:  # Highly influential
        node_colors.append('#4ecdc4')  # Teal
    elif in_degree > 0.1:  # Moderately influenced
        node_colors.append('#ffa07a')  # Light orange
    elif out_degree > 0.1:  # Moderately influential
        node_colors.append('#98d8c8')  # Light teal
    else:  # Standard nodes
        node_colors.append('#f7f7f7')  # Light gray

nx.draw_networkx_nodes(G, pos, 
                      node_size=node_sizes,
                      node_color=node_colors,
                      alpha=0.9,
                      edgecolors='darkred',
                      linewidths=1)

# Add node labels for ALL nodes (no filtering)
labels = {node: G.nodes[node]['label'] for node in G.nodes()}

nx.draw_networkx_labels(G, pos, labels, 
                       font_size=6, 
                       font_weight='bold',
                       font_color='darkred')

# Add title
plt.title('Network Analysis: Layering Invisible Stuff But Influential', 
          fontsize=20, fontweight='bold', pad=20, color='darkred')

# Add legend
legend_elements = [
    mpatches.Patch(color='#ff6b6b', label='Highly Influenced Nodes'),
    mpatches.Patch(color='#4ecdc4', label='Highly Influential Nodes'),
    mpatches.Patch(color='#ffa07a', label='Moderately Influenced'),
    mpatches.Patch(color='#98d8c8', label='Moderately Influential'),
    mpatches.Patch(color='#f7f7f7', label='Standard Nodes'),
    Line2D([0], [0], color='#1f77b4', lw=4, label='Strong Connections (>0.8)'),
    Line2D([0], [0], color='#ff7f0e', lw=4, label='Medium Connections (0.6-0.8)'),
    Line2D([0], [0], color='#2ca02c', lw=4, label='Moderate Connections (0.4-0.6)'),
    Line2D([0], [0], color='#d62728', lw=4, label='Weak Connections (<0.4)')
]

plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))

# Add description text
description = """
This dense network visualizes the complex web of 'invisible' factors that influence hype culture and collectible markets.
Node size indicates overall influence. Color indicates influence type (red=influenced, teal=influential).
Connection colors show strength: Blue=Strong, Orange=Medium, Green=Moderate, Red=Weak.
ALL nodes are connected with clear, color-coded connections showing how these factors layer and reinforce each other.
"""
plt.figtext(0.5, 0.02, description, ha='center', fontsize=10, 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))

# Adjust layout and save
plt.tight_layout()
plt.savefig('network_analysis_fixed.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

# Print network statistics
print("Fixed Network Analysis Statistics:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Network density: {nx.density(G):.3f}")
print(f"Average clustering coefficient: {nx.average_clustering(G):.3f}")

# Check for isolated nodes
isolated_nodes = list(nx.isolates(G))
if isolated_nodes:
    print(f"WARNING: Isolated nodes found: {isolated_nodes}")
else:
    print("✓ All nodes are connected!")

# Print most influential nodes
print("\nMost Influential Nodes (by degree centrality):")
degree_centrality = nx.degree_centrality(G)
for node, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:8]:
    print(f"{G.nodes[node]['label']}: {centrality:.3f}")

# Print minimum connections per node
min_connections = min([G.degree(node) for node in G.nodes()])
print(f"\nMinimum connections per node: {min_connections}") 
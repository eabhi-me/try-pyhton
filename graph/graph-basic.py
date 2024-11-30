class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Dictionary to store the graph: node -> list of neighbors

    def add_node(self, node):
        """Add a new node to the graph if it doesn't exist."""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        """Add an undirected edge between node1 and node2."""
        # Ensure both nodes are in the graph
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)
        
        # Add each node to the other's adjacency list
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def display(self):
        """Display the graph as an adjacency list."""
        for node, neighbors in self.adjacency_list.items():
            print(f"{node}: {neighbors}")

# Example usage
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")

graph.display()

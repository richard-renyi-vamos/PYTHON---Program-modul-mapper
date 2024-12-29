import networkx as nx
import matplotlib.pyplot as plt

class ModuleConnectionMapper:
    def __init__(self):
        """Initialize the mapper with an empty graph."""
        self.graph = nx.DiGraph()

    def add_module(self, module_name):
        """Add a module to the graph if it does not already exist.
        
        Args:
            module_name (str): The name of the module.
        """
        if module_name not in self.graph:
            self.graph.add_node(module_name)
            print(f"Module '{module_name}' added.")
        else:
            print(f"Module '{module_name}' already exists.")

    def add_connection(self, from_module, to_module):
        """Add a connection between two modules.
        
        Args:
            from_module (str): The source module.
            to_module (str): The destination module.
        """
        if from_module in self.graph and to_module in self.graph:
            self.graph.add_edge(from_module, to_module)
            print(f"Connection from '{from_module}' to '{to_module}' added.")
        else:
            print("Both modules must exist before adding a connection.")

    def remove_module(self, module_name):
        """Remove a module and its connections from the graph.
        
        Args:
            module_name (str): The name of the module to remove.
        """
        if module_name in self.graph:
            self.graph.remove_node(module_name)
            print(f"Module '{module_name}' removed.")
        else:
            print(f"Module '{module_name}' does not exist.")

    def visualize(self):
        """Display a graphical representation of the modules and their connections."""
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray',
                node_size=2000, font_size=10, font_weight='bold')
        plt.title("Module Connection Map")
        plt.show()

if __name__ == "__main__":
    mapper = ModuleConnectionMapper()

    print("Welcome to the Module Connection Mapper!")
    while True:
        print("\nOptions:")
        print("1. Add a module")
        print("2. Add a connection")
        print("3. Remove a module")
        print("4. Visualize connections")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            module_name = input("Enter module name: ")
            mapper.add_module(module_name)
        elif choice == "2":
            from_module = input("Enter source module name: ")
            to_module = input("Enter destination module name: ")
            mapper.add_connection(from_module, to_module)
        elif choice == "3":
            module_name = input("Enter module name to remove: ")
            mapper.remove_module(module_name)
        elif choice == "4":
            mapper.visualize()
        elif choice == "5":
            print("Exiting the Module Connection Mapper. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

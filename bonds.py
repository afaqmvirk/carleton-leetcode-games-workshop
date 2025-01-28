def longest_chain(molecule):
    # Initialize an empty graph to represent the molecular structure as an adjacency list.
    # Each carbon atom will be a node, and connections between them will be edges.
    graph = []
    
    # Stack to keep track of branching points (where '(' is encountered).
    branch_stack = []
    
    # Keeps track of the last carbon atom we processed, used to connect subsequent carbons.
    last_carbon = None

    # Step 1: Build the graph from the molecule string.
    for char in molecule:
        if char == 'C':
            # Create a new carbon node with an index equal to the current size of the graph.
            carbon_index = len(graph)
            graph.append([])  # Add an empty list for the new node's neighbors.
            
            if last_carbon is not None:
                # Connect the new carbon to the previous carbon (last_carbon).
                graph[last_carbon].append(carbon_index)
                graph[carbon_index].append(last_carbon)
            
            # Update last_carbon to the current node.
            last_carbon = carbon_index
        
        elif char == '(':
            # Save the current carbon as a branching point by pushing it onto the stack.
            branch_stack.append(last_carbon)
        
        elif char == ')':
            # Return to the last branching point by popping the stack.
            # This ensures the next atoms are connected to the correct branch point.
            last_carbon = branch_stack.pop()

    # Step 2: Define a helper function to perform BFS to find the farthest node.
    def bfs_farthest_node(start_node):
        # Initialize distances for all nodes as -1 (unvisited).
        distances = [-1] * len(graph)
        
        # Mark the starting node as visited with a distance of 0.
        distances[start_node] = 0
        
        # Variable to track the farthest node found during the BFS.
        farthest_node = start_node
        
        # Use a standard list as a queue for BFS.
        queue = [start_node]
        while queue:
            # Pop the first element from the queue (current node).
            current_node = queue.pop(0)
            
            # Explore all neighbors of the current node.
            for neighbor in graph[current_node]:
                if distances[neighbor] == -1:  # If the neighbor hasn't been visited:
                    # Set the distance to one more than the current node's distance.
                    distances[neighbor] = distances[current_node] + 1
                    
                    # Update the farthest node found so far.
                    farthest_node = neighbor
                    
                    # Add the neighbor to the queue for further exploration.
                    queue.append(neighbor)
        
        # Return the farthest node found and its distance from the starting node. 
        return farthest_node, distances[farthest_node]

    # Step 3: Use the BFS function to find the longest chain in the graph.

    # First, find the farthest node from an arbitrary starting node (node 0).
    # This gives us one endpoint of the longest path in the graph.
    first_farthest, _ = bfs_farthest_node(0)

    # Next, perform BFS again starting from the first farthest node.
    # This finds the other endpoint of the longest path and the distance between them.
    second_farthest, max_distance = bfs_farthest_node(first_farthest)

    # The longest chain length is the distance between the two farthest nodes plus 1.
    return max_distance + 1

# Example usage
if __name__ == '__main__':
    molecule = "CCCC(C(CCC(CC(C)C)C)C(CC(CCCCC(C(C)C(C)C)C)C(C(C(C)C)C)))CC(CCC(C(CC(CC(C)C)CC)C(CC(C)C))C)CCC(C(C(CC(C)C(C(C)C)C(C(C)C)))C)"
    print(longest_chain(molecule))


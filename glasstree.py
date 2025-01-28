def count_safe_paths(tree_str):
    # Convert the binary string into a list of integers
    tree = [int(char) for char in tree_str]
    
    def dfs(index):
        # If index is out of bounds, return 0 (no paths).
        if index >= len(tree):
            return 0
        
        # If the current tile is dangerous, terminate this path.
        if tree[index] == 0:
            return 0
        
        # If it's a leaf node (no children), return 1 (safe path).
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child >= len(tree) and right_child >= len(tree):
            return 1
        
        # Recursively calculate safe paths for left and right children.
        return dfs(left_child) + dfs(right_child)

    # Start DFS from the root (index 0).
    return dfs(0)


# Example usage
tree_input = "11111111111111111111111000010111011010111111110010001011110111111111101111101011111100101101111001100110111101110111111110001110110111111111100001011101101011111111001000101111011111111110111110101111110010110111100110011011110111011111111000111011011111"  # Replace with your input
print(count_safe_paths(tree_input))

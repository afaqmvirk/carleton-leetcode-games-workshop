def count_safe_paths(tree: str) -> int:
    n = len(tree)
    
    def dfs(index):
        if index >= n or tree[index] == "0":
            return 0

        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child >= n and right_child >= n:
            return 1

        return dfs(left_child) + dfs(right_child)

    return dfs(0)


print(count_safe_paths("11111111111111111111111000010111011010111111110010001011110111111111101111101011111100101101111001100110111101110111111110001110110111111111100001011101101011111111001000101111011111111110111110101111110010110111100110011011110111011111111000111011011111"))


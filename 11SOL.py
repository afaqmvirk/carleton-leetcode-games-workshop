def ddakji_flip_count_and_orientation(flips: str):
    # Define the initial orientation as a 1D array
    original_orientation = ["A", "B", "C", "D"]
    current_orientation = ["A", "B", "C", "D"]
    flip_count = 0  # Count how many times it returns to the original orientation

    # Map to track the effects of flips
    vertical_flip = [2, 3, 0, 1]   # Swap top and bottom rows
    horizontal_flip = [1, 0, 3, 2]  # Swap left and right columns

    for flip in flips:
        if flip == "V":
            # Apply vertical flip
            current_orientation = [current_orientation[i] for i in vertical_flip]
        elif flip == "H":
            # Apply horizontal flip
            current_orientation = [current_orientation[i] for i in horizontal_flip]

        # Check if the current orientation matches the original
        if current_orientation == original_orientation:
            flip_count += 1

    # Return the results
    return flip_count, current_orientation


# Sample input
flips = "HHHHVHHHHHHVHVHHHHHHHVVVHVVHHVHHVVHVHVVVHHVVVHVHHHVHHVVHVVVHHVVHHHVHVVHVHVVVVHHHVVVHHHHVVVVVHHVVVHVHVVVVHHHHVHVHHHVVHVHHHHVHHHHVVVVVHHVHVHHVHHHVVVHVVHHHHVVVHHVHHHVHHVVHHVHVVVVVVHHHVHVVHHVHVHVHVVHVHHHVVHVVVHHVHVVHHHVHHVHVHVHVVHHVVHHHHHVVHVVVHVVHVHVHVHVHVHVHVHVHHVVHVHVVHHHVHVVHHHVHVHVHVHVVVHVVVHVHHVVHVHHVHHVHVVHVVVVVHHVVHHVVHVVHVHVVHHVHHVHHVVHVVVHHHVVHVHVHHHHVVVHVVVHVHHHVVVHVVVHVHVHHHHHHHHHHHVHHVVVHVHVHVHHVHHHHHVHVHHVHVVVHHVHVVVHVVVVVHVHHVHVHVHVVHVHVVVVVVVHHVHVHHHVVVVHVHHHVVVVVVVHVHVHVVVVHHVVVVVVHHHHVVVHHVVVHVVHVHHHVHVHHHVHHHVVHHVHVHVVVVHVVVVVVVHHHHHVVVHHHVVVVHHVHHVVHHVHVVHVVVVHHVVVVVHVVVVHVHHHVHHVHVHHVHVHHVHVVVVVVVVHVVVVVHHHVHHHHVHHVVVHVVVVVHVVHVHHVVVHHHHHVHVVVHHHVVVVVHHHHHVHHVHHVVVHVHHHHHVVHHHHVHVVHVVHHVHHVHHHVHHHVVHHVHHVHHVVHHVHVVHVHHHHHVVVVVHVVHVHHHHVHHVVVVHVVHVHHHHHHVHHHVVHVHHHVVVHHVHVHVVVVVVHVHVHVVVVHHHHVVHVHVHHHHVVHVVVHVHHHVVHHVVHHVHHVVHHHHHVVHHVVHVVHVHHVVHVVVHHVVVHHHHVHHVHHVVVHVVHVVHVHHHHHHHHVVHHVVVHHHHVVVVHHHVVHHVHHVVVHHHHVVVVVVHHVHHVVVVVHVVHVVVHVHVHVHHHVVVHHVHVHHVHVHVHVHVVHVVHH"

# Solve the problem
flip_count, final_orientation = ddakji_flip_count_and_orientation(flips)

# Print results
print(flip_count)
print(f"{final_orientation[0]} {final_orientation[1]}")
print(f"{final_orientation[2]} {final_orientation[3]}")

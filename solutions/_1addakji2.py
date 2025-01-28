def ddakji_flips_check(s: str) -> str:
    # Track whether the ddakji has been flipped vertically or horizontally
    vertical_flips = 0
    horizontal_flips = 0
    original_count = 0

    # Process the flip sequence
    for flip in s:
        if flip == "V":
            vertical_flips += 1
        elif flip == "H":
            horizontal_flips += 1

        # Check if the ddakji is back to the original orientation
        if vertical_flips % 2 == 0 and horizontal_flips % 2 == 0:
            original_count += 1

    # Determine the final orientation
    if vertical_flips % 2 == 0 and horizontal_flips % 2 == 0:
        final_grid = "A B\nC D"
    elif vertical_flips % 2 == 1 and horizontal_flips % 2 == 0:
        final_grid = "C D\nA B"
    elif vertical_flips % 2 == 0 and horizontal_flips % 2 == 1:
        final_grid = "B A\nD C"
    elif vertical_flips % 2 == 1 and horizontal_flips % 2 == 1:
        final_grid = "D C\nB A"

    # Exclude the initial position from the count
    original_count = max(0, original_count)
    print(f"{original_count}\n{final_grid}")


# Example usage
ddakji_flips_check("HVVHVHVHVVVHVVHVHHVHVHHVHHHHHVVVVHHVHHHHHVVHVHHVVHVHHHVHHVHVVVHVHHHVHVVHVVVHHHHHHVVHHHVVVHHHVHVVVHVVVVHHVHVVVHHHVHVHHHHVVHHHHVHHVHVVVVHVHVHHHVVHHVVHHVVVVHVHVHHHHVVVVHVVHHHHHHVHVHHVHHVVHHHHVHHHVVHVVVHVHHHVHHHHVVVHHVHVHVHHHVHHHVHHHHHVVVHVHVVHHVVHHVVVVVHHVVVVVHVVVHVVHVHVHHHHHVHVVVHVHHVVHHVVVVHHHVHHVHVHHVVVVVHHHHVVHHHHHVVHHHVHHVHHHVVHVHHHHHHVHHVHVVHVHHHVHVHVVHVVHVHHHVHVHVHVVVHVHHHVHVVVHHVVVHVHVVVHHVHHHHHVVHHHHHVHHVVHVVVHHVHHVHHHVVHVVVHVHVHVHVVHVHHHHHHVHVVV")
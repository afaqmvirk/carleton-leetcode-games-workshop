def ddakji_flips(s: str):
    orientation = ["A", "B", "C", "D"] 
    original_orientation = orientation[:]
    original_count = 0 

    for flip in s:
        if flip == "V":
            orientation = [orientation[2], orientation[3], orientation[0], orientation[1]]
        elif flip == "H":
            orientation = [orientation[1], orientation[0], orientation[3], orientation[2]]
        if orientation == original_orientation:
            original_count += 1

    final_grid = f"{orientation[0]} {orientation[1]}\n{orientation[2]} {orientation[3]}"

    print(original_count, "\n" + final_grid)


ddakji_flips("HVVHVHVHVVVHVVHVHHVHVHHVHHHHHVVVVHHVHHHHHVVHVHHVVHVHHHVHHVHVVVHVHHHVHVVHVVVHHHHHHVVHHHVVVHHHVHVVVHVVVVHHVHVVVHHHVHVHHHHVVHHHHVHHVHVVVVHVHVHHHVVHHVVHHVVVVHVHVHHHHVVVVHVVHHHHHHVHVHHVHHVVHHHHVHHHVVHVVVHVHHHVHHHHVVVHHVHVHVHHHVHHHVHHHHHVVVHVHVVHHVVHHVVVVVHHVVVVVHVVVHVVHVHVHHHHHVHVVVHVHHVVHHVVVVHHHVHHVHVHHVVVVVHHHHVVHHHHHVVHHHVHHVHHHVVHVHHHHHHVHHVHVVHVHHHVHVHVVHVVHVHHHVHVHVHVVVHVHHHVHVVVHHVVVHVHVVVHHVHHHHHVVHHHHHVHHVVHVVVHHVHHVHHHVVHVVVHVHVHVHVVHVHHHHHHVHVVV")
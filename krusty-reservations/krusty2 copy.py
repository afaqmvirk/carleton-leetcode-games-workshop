def max_reservations_with_capacity(capacity, reservations):
    usage = [0] * 24
    n = len(reservations)
    best_count = 0  # Global best (maximum) accepted reservations so far.

    def can_accept(s, e, seats):
        for t in range(s, e):
            if usage[t] + seats > capacity:
                return False
        return True

    def add_reservation(s, e, seats):
        for t in range(s, e):
            usage[t] += seats

    def remove_reservation(s, e, seats):
        for t in range(s, e):
            usage[t] -= seats

    def backtrack(i, current_count):
        nonlocal best_count
        
        if i == n:
            best_count = max(best_count, current_count)
            return
        
        backtrack(i + 1, current_count)

        s, e, seats = reservations[i]
        if can_accept(s, e, seats):
            add_reservation(s, e, seats)
            backtrack(i + 1, current_count + 1)
            remove_reservation(s, e, seats)
    backtrack(0, 0)
    return best_count


if __name__ == "__main__":
    # Example of reading input:
    # First line: integer capacity
    # Next lines: reservations in the form (S, E, N)
    #
    # For the sample, let's hardcode or parse as needed.

    # Sample input interpretation:
    # capacity = 6
    # reservations = [(9, 12, 4), (3, 6, 1), (4, 5, 2), (1, 3, 3)]

    capacity = 6
    reservations = [
        (9, 12, 4),
        (15, 18, 1),
(16, 17, 2),
(12, 15, 3)

    ]

    # Compute and print the result
    answer = max_reservations_with_capacity(capacity, reservations)
    print(answer)  # Expect 4 for the sample

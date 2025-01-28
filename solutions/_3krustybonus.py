def max_reservations_with_capacity(capacity, reservations):
    """
    :param capacity: (int) The total seating capacity of the Krusty Krab.
    :param reservations: (list of tuples) Each tuple is (S, E, N) where
                        S = start hour, E = end hour (exclusive), N = seats required.
    :return: (int) The maximum number of reservations that can be accepted.
    """
    
    # We'll track usage of seats by the hour in a list of length 24 (0..23).
    # If you're certain times are always in [0..23], this is sufficient.
    usage = [0] * 24
    n = len(reservations)
    best_count = 0  # Global best (maximum) accepted reservations so far.

    # Sort reservations if desired (not strictly required here).
    # For example, you could sort by end time to *possibly* speed up pruning:
    # reservations.sort(key=lambda x: x[1])

    def can_accept(s, e, seats):
        """Check if we can accept this reservation without exceeding capacity."""
        for t in range(s, e):
            if usage[t] + seats > capacity:
                return False
        return True

    def add_reservation(s, e, seats):
        """Mark usage for accepting a reservation."""
        for t in range(s, e):
            usage[t] += seats

    def remove_reservation(s, e, seats):
        """Revert usage after backtracking."""
        for t in range(s, e):
            usage[t] -= seats

    def backtrack(i, current_count):
        nonlocal best_count
        
        # If we've considered all reservations, update best_count.
        if i == n:
            best_count = max(best_count, current_count)
            return
        
        # ----- Option A: Skip this reservation -----
        backtrack(i + 1, current_count)

        # ----- Option B: Try to accept the reservation if feasible -----
        s, e, seats = reservations[i]
        if can_accept(s, e, seats):
            # Accept it
            add_reservation(s, e, seats)
            backtrack(i + 1, current_count + 1)
            # Backtrack (undo)
            remove_reservation(s, e, seats)

    # Start backtracking from reservation index 0, with 0 accepted so far
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
        (3, 6, 1),
        (4, 5, 2),
        (1, 3, 3)
    ]

    # Compute and print the result
    answer = max_reservations_with_capacity(capacity, reservations)
    print(answer)  # Expect 4 for the sample

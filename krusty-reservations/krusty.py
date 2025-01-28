def line_sweep_in_given_order(reservations, capacity):
    """
    Processes reservations in the exact order given (no sorting).
    Accept a reservation if and only if it fits the seating capacity 
    for all hours it spans, then proceed to the next one.

    :param reservations: list of (start, end, seats) tuples 
                         (hours are assumed to be in [0..23], 
                          though we only care about 9..23 open hours).
    :param capacity: integer, the Krusty Krab's total seating capacity.
    :return: number of reservations accepted.
    """

    # We’ll track seat usage for each hour in [0..23].
    # If you want to restrict strictly to [9..23], you can just store usage[9..23].
    usage = [0] * 24

    accepted_count = 0

    for (start, end, needed_seats) in reservations:
        # 1) Check if there's room for all hours from start..(end-1)
        can_accept = True
        for hour in range(start, end):
            if usage[hour] + needed_seats > capacity:
                can_accept = False
                break

        # 2) If we can accept it, mark the seat usage
        if can_accept:
            for hour in range(start, end):
                usage[hour] += needed_seats
            accepted_count += 1

    return accepted_count


if __name__ == "__main__":
    # Example usage:
    # Suppose the input is given in this arbitrary order:
    # (Note that they may or may not be in ascending start-time order)
    capacity = 30
     

    reservations_in_given_order = [
    # 1. Non-overlapping reservations
    (9, 11, 10), (11, 13, 15), (13, 15, 20), (15, 17, 25), (17, 19, 30), 

    # 2. Fully overlapping reservations
    (10, 12, 20), (10, 12, 10), (10, 12, 15), (10, 12, 30), 

    # 3. Partially overlapping reservations
    (9, 12, 15), (11, 14, 10), (13, 16, 20), (15, 18, 25), (17, 20, 15), 

    # 4. Single-hour reservations
    (9, 10, 5), (10, 11, 3), (11, 12, 7), (12, 13, 2), (23, 24, 1), 

    # 5. Back-to-back reservations
    (9, 11, 10), (11, 13, 15), (13, 15, 20), (15, 17, 25), 

    # 6. Edge-of-capacity reservations
    (12, 14, 30), (14, 16, 25), (16, 18, 20), (18, 20, 15), 

    # 7. Full-day reservations
    (9, 23, 30), (9, 23, 25), (9, 23, 10), 

    # 8. Sparse reservations
    (9, 11, 5), (13, 15, 8), (17, 19, 10), 

    # 9. Dense reservations
    (9, 10, 10), (10, 11, 10), (11, 12, 10), (12, 13, 10), (13, 14, 10), 

    # 10. Complex overlaps
    (9, 12, 15), (10, 13, 20), (11, 14, 25), (12, 15, 30), (13, 16, 15), 

    # 11. Peak-hour reservations
    (18, 21, 30), (19, 22, 25), (20, 23, 20), 

    # 12. Large reservations mixed with small ones
    (9, 12, 30), (9, 12, 5), (10, 11, 10), (10, 11, 2), 

    # 13. Random small reservations
    (9, 10, 1), (10, 11, 1), (11, 12, 1), (12, 13, 1), (13, 14, 1), 

    # 14. Overlapping single-hour reservations
    (9, 10, 10), (9, 10, 5), (9, 10, 15), (9, 10, 20), (9, 10, 30), 

    # 15. Back-to-back edge cases
    (13, 15, 30), (15, 17, 30), (17, 19, 30), 

    # 16. Long but sparse
    (9, 15, 10), (15, 21, 10), 

    # 17. Edge-of-capacity over multiple intervals
    (10, 13, 30), (13, 16, 30), (16, 19, 30), 

    # 18. Random long intervals
    (9, 18, 15), (9, 18, 10), (9, 18, 20), 

    # 19. Single-hour near closing
    (22, 23, 5), (22, 23, 10), (22, 23, 15), 

    # 20. Complex overlaps near capacity
    (9, 12, 20), (10, 13, 25), (11, 14, 30), 

    # 21. Single customer fills capacity for long hours
    (9, 23, 30), 

    # 22. Scattered random reservations
    (9, 10, 3), (12, 13, 7), (15, 16, 12), (18, 19, 18), 

    # 23. Random one-hour overlaps
    (9, 10, 5), (9, 10, 10), (9, 10, 15), (9, 10, 20), 

    # 24. Small reservations spanning many hours
    (9, 11, 5), (11, 13, 5), (13, 15, 5), (15, 17, 5), 

    # 25. Peak overlap with random intervals
    (18, 21, 20), (19, 22, 25), (20, 23, 10), 

    # 26. Last-minute reservations
    (22, 23, 5), (22, 23, 10), (22, 23, 15), 

    # 27. Random one-hour non-overlapping
    (9, 10, 5), (10, 11, 7), (11, 12, 9), (12, 13, 11), (13, 14, 13), 

    # 28. Overlapping small reservations
    (9, 10, 10), (9, 10, 5), (9, 10, 15), 
]


    # We'll accept or reject each in the order shown above.
    answer = line_sweep_in_given_order(reservations_in_given_order, capacity)
    print(answer)

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
     

    reservations_in_given_order = []


    # We'll accept or reject each in the order shown above.
    answer = line_sweep_in_given_order(reservations_in_given_order, capacity)
    print(answer)

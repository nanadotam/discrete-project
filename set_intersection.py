def intersection(*args):
    """
    Compute the intersection of sets.

    Args:
        *args (set): Any number of sets.

    Returns:
        list: The intersection of the sets.
    """
    # Checks if there are at least two sets
    if len(args) < 2:
        raise ValueError("Intersection requires at least two sets")

    intersect = []
    # Iterate through each element in the first set
    for element in args[0]:
        # Check if the element is present in all other sets
        present_in_all = True
        for s in args[1:]:
            if element not in s:
                present_in_all = False
                break
        # If the element is present in all sets, add it to the intersection
        if present_in_all:
            intersect.append(element)

    return intersect


# Example usage
def main():
    set1 = {1, 2, 3, 4, 5, 9}
    set2 = {3, 4, 5, 6, 7, 9}
    set3 = {5, 6, 7, 8, 9}

    result = intersection(set1, set2, set3)
    print("Intersection:", result)


if __name__ == "__main__":
    main()

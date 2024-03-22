def complement(set1, universal_set):
    """
    Compute the complement of a set with respect to a universal set.

    Args:
        set1 (set): The set for which the complement is to be computed.
        universal_set (set): The universal set.

    Returns:
        list: The complement of the set with respect to the universal set.
    """
    # Initialize the complement as an empty list
    complement = []

    # Iterate through each element in the universal set
    for element in universal_set:
        # If the element is not in set1, add it to the complement
        if element not in set1:
            complement.append(element)

    return complement


# Example usage:
def main():
    set1 = {1, 2, 3, 4, 5, 9}
    universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    result = complement(set1, universal_set)
    print("Complement:", result)


if __name__ == "__main__":
    main()

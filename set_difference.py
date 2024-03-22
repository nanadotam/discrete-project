def difference(set1, *args):
    """
    Compute the difference of sets.

    Args:
        set1 (set): The first set.
        *args (set): Any number of sets.

    Returns:
        list: The difference of the sets.
    """
    # Initialize result as a copy of set1
    result = set(set1)

    # Iterate through each set in args
    for s in args:
        # Remove elements present in s from result
        for element in s:
            if element in result:
                result.remove(element)

    return list(result)


# Example Usage
def main():
    set1 = {1, 2, 3, 4, 5, 9}
    set2 = {3, 4, 6, 7, 9}
    set3 = {6, 7, 8, 9}

    result = difference(set1, set2, set3)
    print("Difference:", result) 

if __name__ == "__main__":
    main()
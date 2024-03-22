# *args takes any number of arguments
def union(*args):
    """
    Compute the union of sets.

    Args:
        *args (set): Any number of sets.

    Returns:
        set: The union of the sets.
    """
    
    # Stores the union of the sets
    result = set()
    # Updates elements of the set (ensuring there are no duplicates)
    for s in args:
        result.update(s)
    return result

# Example Usage
def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    set3 = {5, 6, 7, 8, 9}

    result = union(set1, set2, set3)
    print("Union:", result)

if __name__ == "__main__":
    main()

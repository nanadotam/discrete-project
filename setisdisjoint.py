def setisdisjoint(s1, s2, *args):
    """
    Checks if two sets are disjoint.

    Args:
        s1 (set): The first set.
        s2 (set): The second set.
        *args (set): Any number of sets.

    Returns:
        bool: True if the sets are disjoint, False otherwise.
    """
    sets = [s1, s2] + list(args)
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            disjoint = True
            for elem in sets[i]:
                if elem in sets[j]:
                    disjoint = False
                    break
            if disjoint:
                continue
            else:
                return False
    return True

# Example usage:
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(setisdisjoint(set1, set2))  # Output: True
print(setisdisjoint(set1, set3))  # Output: False

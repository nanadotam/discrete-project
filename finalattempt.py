# import required modules
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3, venn2_unweighted

# Built-in functions for set union, intersections, complement, and difference
# Set Complement
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


# # Example usage:
# def main():
#     set1 = {1, 2, 3, 4, 5, 9}
#     universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#     result = complement(set1, universal_set)
#     print("Complement:", result)


# if __name__ == "__main__":
#     main()

#  Set Union
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

# # Example Usage
# def main():
#     set1 = {1, 2, 3, 4, 5}
#     set2 = {3, 4, 5, 6, 7}
#     set3 = {5, 6, 7, 8, 9}

#     result = union(set1, set2, set3)
#     print("Union:", result)

# if __name__ == "__main__":
#     main()

# Set intersection
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


# # Example usage
# def main():
#     set1 = {1, 2, 3, 4, 5, 9}
#     set2 = {3, 4, 5, 6, 7, 9}
#     set3 = {5, 6, 7, 8, 9}

#     result = intersection(set1, set2, set3)
#     print("Intersection:", result)


# if __name__ == "__main__":
#     main()

# Set Difference
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

# # Example usage:
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# set3 = {3, 4, 5}
# print(setisdisjoint(set1, set2))  # Output: True
# print(setisdisjoint(set1, set3))  # Output: False


# # Example Usage
# def main():
#     set1 = {1, 2, 3, 4, 5, 9}
#     set2 = {3, 4, 6, 7, 9}
#     set3 = {6, 7, 8, 9}

#     result = difference(set1, set2, set3)
#     print("Difference:", result) 

# if __name__ == "__main__":
#     main()

# Main Program logic and functionality
# basic program functionality

# take user input
# set1 = set(input("Enter elements of set 1 separated by commas: ").split(","))
set1 = {1,2,3,4,5}
# print(set1)
# set2 = set(input("Enter elements of set 2 separated by commas: ").split(","))
set2 = {4,5,6,7,8}
set3 = {10, 11, 12, 14}

# plot the venn diagram using venn2_unweighted
venn = venn2_unweighted(subsets=(set1, set2), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)

venn.get_label_by_id('10').set_text('\n'.join(map(str, set1-set2)))
# intersection
venn.get_label_by_id('11').set_text('\n'.join(map(str, set1&set2)))

venn.get_label_by_id('01').set_text('\n'.join(map(str, set2-set1)))

# make the members write outside the circle
# venn.get_label_by_id('110').set_text('\n'.join(map(str, set3)))


# Add a title
plt.title("Basic two Venn Diagrams")

# Show the plot
plt.show()

# test for intersection 
print("\nIntersection of sets:\n",intersection(set1,set2))

# find the difference between sets

'''
because we cant plot our intersection simply like that,
we can hard-code it  by putting it inside the middle position of the program
(the middle part of the venn diagram)
'''


# check if set is disjoint
if setisdisjoint(set1, set2):
    venn_3 = venn2_unweighted(subsets=(set1, set2, 0), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)
    # put set 1 in its own section
    venn_3.get_label_by_id('10').set_text('\n'.join(map(str, set1)))

    # set 2 in its own section
    venn_3.get_label_by_id('01').set_text('\n'.join(map(str, set1)))
    
    # Add a title
    plt.title("Basic two Venn Diagrams Disjoint")

    # Show the plot
    plt.show()

# make the text write outside the circles
    



# maybe try highlighting the middle parts for only intersections
venn = venn2_unweighted(subsets=(set1, set2), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)

venn.get_label_by_id('10').set_text('\n'.join(map(str, set1-set2)))
# intersection
venn.get_label_by_id('11').set_text('\n'.join(map(str, set1&set2)))

venn.get_label_by_id('01').set_text('\n'.join(map(str, set2-set1)))
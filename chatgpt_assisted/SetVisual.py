import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
 
import numpy as np

def visualize_set_operations(sets, operation):
    # Convert sets to numerical values representing sizes of subsets
    subset_sizes = {int(key, 2): len(val) for key, val in sets.items()}
    
    # Create a Venn diagram based on the sets and operation
    if operation == 'union':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=('Set A', 'Set B'))
    elif operation == 'intersection':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=('Set A', 'Set B'), set_colors=('skyblue', 'lightgreen'))
    elif operation == 'difference':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=('Set A', 'Set B'), set_colors=('skyblue', 'lightgreen'))
    elif operation == 'complement':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=('Set A', 'Set B'), set_colors=('skyblue', 'lightgreen'))
    
    # Display the Venn diagram
    plt.title(operation.capitalize() + " of Sets")
    plt.show()


def main():
    # Input sets
    set_A = set(input("Enter elements of set A separated by space: ").split())
    set_B = set(input("Enter elements of set B separated by space: ").split())
    
    # Convert sets to lists for visualization
    set_A_list = list(set_A)
    set_B_list = list(set_B)
    
    # Perform set operations
    sets = {'10': set_A, '01': set_B, '11': set_A.intersection(set_B), '00': set()}
    
    print("Choose set operation:")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference (A - B)")
    print("4. Difference (B - A)")
    print("5. Complement of A")
    print("6. Complement of B")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        visualize_set_operations(sets, 'union')
    elif choice == 2:
        visualize_set_operations(sets, 'intersection')
    elif choice == 3:
        sets['10'] = set_A - set_B
        visualize_set_operations(sets, 'difference')
    elif choice == 4:
        sets['01'] = set_B - set_A
        visualize_set_operations(sets, 'difference')
    elif choice == 5:
        sets['00'] = set_B - set_A
        visualize_set_operations(sets, 'complement')
    elif choice == 6:
        sets['00'] = set_A - set_B
        visualize_set_operations(sets, 'complement')
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

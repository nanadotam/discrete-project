import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles

def visualize_set_operations(sets, operation):
    subset_sizes = {key: len(val) for key, val in sets.items()}
    
    if operation == 'union':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=tuple(sets.keys()))
    elif operation == 'intersection':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=tuple(sets.keys()), set_colors=('skyblue', 'lightgreen'))
    elif operation == 'difference':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=tuple(sets.keys()), set_colors=('skyblue', 'lightgreen'))
    elif operation == 'complement':
        venn_diagram = venn2(subsets=subset_sizes, set_labels=tuple(sets.keys()), set_colors=('skyblue', 'lightgreen'))
    
    plt.title(operation.capitalize() + " of Sets")
    plt.show()

def main():
    num_sets = int(input("Enter the number of sets: "))
    sets = {}
    
    for i in range(num_sets):
        set_name = input(f"Enter elements of set {chr(65+i)} separated by space: ")
        sets[chr(65+i)] = set(set_name.split())
    
    choice = int(input("Choose set operation:\n1. Union\n2. Intersection\n3. Difference (A - B)\n4. Difference (B - A)\n5. Complement of A\n6. Complement of B\nEnter your choice: "))
    
    if choice in [1, 2]:
        visualize_set_operations(sets, 'union' if choice == 1 else 'intersection')
    elif choice in [3, 4]:
        sets[list(sets.keys())[0] + list(sets.keys())[1]] = sets['A'] - sets['B'] if choice == 3 else sets['B'] - sets['A']
        visualize_set_operations(sets, 'difference')
    elif choice in [5, 6]:
        sets['00'] = sets['B'] - sets['A'] if choice == 5 else sets['A'] - sets['B']
        visualize_set_operations(sets, 'complement')
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

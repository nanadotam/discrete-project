#  Add try catch exceptions


def draw_venn_diagram(sets, operation):
    # Find the elements in each set
    A = sets['A']
    B = sets['B']
    
#  complement
    # unoiversal set and that set for complement


    # Initialize the set for the Venn diagram regions
    AB = A.intersection(B)
    A_B = A.difference(B)
    B_A = B.difference(A)
    A_c = A.symmetric_difference(AB)
    B_c = B.symmetric_difference(AB)
    
    # Create a grid for the Venn diagram
    venn_grid = [
        [A_c, A_B, A],
        [B_A, AB, B]
    ]
    
    # Create labels for the Venn diagram regions
    labels = {
        'A': A_c,
        'B': B_c,
        'A_B': A_B,
        'B_A': B_A,
        'AB': AB,
        'A_B_A': A.intersection(B_A),
        'A_AB': A.intersection(AB),
        'A_B_AB': A_B.intersection(AB),
        'B_A_AB': B_A.intersection(AB)
    }
    
    # Print the Venn diagram
    print("A:", A)
    print("B:", B)
    print("A {}: {}".format(operation, labels[operation]))
    print("-----")
    print("| A   B |")
    print("| {} {} |".format(len(labels['A_B_A']), len(labels['A_AB'])))
    print("| {} {} |".format(len(labels['B_A']), len(labels['AB'])))
    print("-----")
    
def main():
    num_sets = int(input("Enter the number of sets: "))
    sets = {}
    
    for i in range(num_sets):
        set_name = input(f"Enter elements of set {chr(65+i)} separated by space: ")
        sets[chr(65+i)] = set(set_name.split())
    
    choice = int(input("Choose set operation:\n1. Union\n2. Intersection\n3. Difference (A - B)\n4. Difference (B - A)\n5. Complement of A\n6. Complement of B\nEnter your choice: "))
    
    if choice == 1:
        draw_venn_diagram(sets, 'AB')
    elif choice == 2:
        draw_venn_diagram(sets, 'A_B')
    elif choice == 3:
        draw_venn_diagram(sets, 'A_B')
    elif choice == 4:
        draw_venn_diagram(sets, 'B_A')
    elif choice == 5:
        draw_venn_diagram(sets, 'A')
    elif choice == 6:
        draw_venn_diagram(sets, 'B')
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

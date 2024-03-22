import matplotlib.pyplot as plt

def draw_venn_diagram(sets, operation):
    A = sets['A']
    B = sets['B']
    
    # Find the elements in each set operation
    if operation == 'AB':
        AB = A.intersection(B)
        A_B = A.difference(B)
        B_A = B.difference(A)
        AB = A.intersection(B)
        A_B = A.difference(B)
        B_A = B.difference(A)
    elif operation == 'B_A':
        AB = A.intersection(B)
        A_B = A.difference(B)
        B_A = B.difference(A)
    elif operation == 'A':
        AB = A.intersection(B)
        A_B = A.difference(B)
        B_A = B.difference(A)
    elif operation == 'B':
        AB = A.intersection(B)
        A_B = A.difference(B)
        B_A = B.difference(A)
    else:
        print("Invalid operation")
        return
    
    # Create Venn diagram using Matplotlib
    plt.figure(figsize=(8, 8))
    plt.title("Venn Diagram")
    plt.text(-0.5, 0.5, 'A - B', fontsize=12)
    plt.text(0.5, 0.5, 'A & B', fontsize=12)
    plt.text(0, -0.5, 'B - A', fontsize=12)
    plt.text(0, 0, 'A', fontsize=12)
    plt.text(0, 0, 'B', fontsize=12)
    plt.text(0, 0, 'A & B', fontsize=12)
    plt.text(0, 0, 'A - B', fontsize=12)
    plt.text(0, 0, 'B - A', fontsize=12)
    
    # Circles
    plt.scatter(x=[0, 0.5, 0], y=[0, 0.5, 0], s=150000, color=["red", "green", "purple"], alpha = 0.3)

    plt.axis('off')
    plt.show()

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

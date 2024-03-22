import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import numpy as np

from set_intersection import intersection







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

import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

from set_intersection import intersection
from set_union import union
from set_difference import difference
from set_complement import complement



universal_set = set(input("Enter elements of the Universal set separated by space: ").split())
set1 = set(input("Enter elements of set A separated by space: ").split())
set2 = set(input("Enter elements of set B separated by space: ").split())

# Call functions for set operations
union(set1, set2)
intersection(set1, set2)
difference(set1, set2)
complement(set1, universal_set)

# Define GUI
def perform_operation():
    operation = operation_var.get()
    set1 = set(text_entry1.get().split(','))
    set2 = set(text_entry2.get().split(','))
    universal_set = set(text_entry_universal.get().split(','))

    if operation == 'Union':
        result_set = union(set1, set2)
    elif operation == 'Intersection':
        result_set = intersection(set1, set2)
    elif operation == 'Difference':
        result_set = difference(set1, set2)
    elif operation == 'Complement':
        result_set = complement(set1, universal_set)
    
    # Visualize the result
    visualize_result(result_set, set1, set2)

def visualize_result(result_set, set1, set2):
    plt.figure()
    if len(set1) == 2 and len(set2) == 2:
        venn2([set1, set2], ('Set 1', 'Set 2'))
    elif len(set1) == 3 and len(set2) == 3:
        venn3([set1, set2], ('Set 1', 'Set 2'))
    plt.title('Venn Diagram')
    plt.show()

# Create GUI
root = tk.Tk()
root.geometry("500x500")
root.title('Set Visualization Tool')

# Input for sets
tk.Label(root, text="Set 1:").grid(row=0, column=0)
text_entry1 = tk.Entry(root)
text_entry1.grid(row=0, column=1)

tk.Label(root, text="Set 2:").grid(row=1, column=0)
text_entry2 = tk.Entry(root)
text_entry2.grid(row=1, column=1)

tk.Label(root, text="Universal Set:").grid(row=2, column=0)
text_entry_universal = tk.Entry(root)
text_entry_universal.grid(row=2, column=1)

# Dropdown for set operations
tk.Label(root, text="Operation:").grid(row=3, column=0)
operation_var = tk.StringVar(root)
operation_var.set("Union")  # Default value
operations = ['Union', 'Intersection', 'Difference', 'Complement']
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=3, column=1)

# Button to perform operation
perform_button = tk.Button(root, text="Perform Operation", command=perform_operation)
perform_button.grid(row=4, column=0, columnspan=2)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib_venn import venn2_unweighted

def union(*sets):
    """
    Compute the union of sets.

    Args:
        *sets (set): Any number of sets.

    Returns:
        set: The union of the sets.
    """
    return set().union(*sets)

def intersection(*sets):
    """
    Compute the intersection of sets.

    Args:
        *sets (set): Any number of sets.

    Returns:
        set: The intersection of the sets.
    """
    return set.intersection(*sets)

def difference(set1, *sets):
    """
    Compute the difference of sets.

    Args:
        set1 (set): The first set.
        *sets (set): Any number of sets.

    Returns:
        set: The difference of the sets.
    """
    result = set1.copy()
    for s in sets:
        result.difference_update(s)
    return result

def plot_venn(set1, set2, operation):
    """
    Plot Venn diagram for given sets and operation.

    Args:
        set1 (set): First set.
        set2 (set): Second set.
        operation (str): Operation to be performed (union, intersection, difference).
    """
    if operation == "union":
        venn = venn2_unweighted(subsets=(set1, set2), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)
    elif operation == "intersection":
        venn = venn2_unweighted(subsets=(set1, set2), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)
        venn.get_label_by_id('10').set_text('\n'.join(map(str, set1-set2)))
        venn.get_label_by_id('11').set_text('\n'.join(map(str, set1&set2)))
        venn.get_label_by_id('01').set_text('\n'.join(map(str, set2-set1)))
    elif operation == "difference":
        venn = venn2_unweighted(subsets=(set1, set2), set_labels=('Set 1', 'Set 2'), set_colors=("blue", "pink"), alpha=0.7)
        venn.get_label_by_id('10').set_text('\n'.join(map(str, set1-set2)))
    plt.title(f"{operation.capitalize()} of Sets")
    plt.show()

def validate_sets(input_sets):
    """
    Validate sets entered by the user.

    Args:
        input_sets (str): Sets entered by the user as comma-separated strings.

    Returns:
        list: List of validated sets.
    """
    sets = []
    for input_set in input_sets:
        try:
            sets.append(set(map(int, input_set.split(","))))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter integers separated by commas.")
            return None
    return sets

def perform_operation():
    """
    Perform set operation selected by the user.
    """
    set1_input = entry_set1.get()
    set2_input = entry_set2.get()

    # Validate input sets
    input_sets = validate_sets([set1_input, set2_input])
    if input_sets is None:
        return

    set1, set2 = input_sets

    operation = operation_var.get()
    if operation == "union":
        result = union(set1, set2)
    elif operation == "intersection":
        result = intersection(set1, set2)
    elif operation == "difference":
        result = difference(set1, set2)
    else:
        messagebox.showerror("Error", "Invalid operation selected.")
        return

    # Plot Venn diagram
    plot_venn(set1, set2, operation)

# Create main window
root = tk.Tk()
root.title("Set Operations Visualizer")

# Set 1 input
label_set1 = tk.Label(root, text="Enter elements of set 1 separated by commas:")
label_set1.pack()
entry_set1 = tk.Entry(root)
entry_set1.pack()

# Set 2 input
label_set2 = tk.Label(root, text="Enter elements of set 2 separated by commas:")
label_set2.pack()
entry_set2 = tk.Entry(root)
entry_set2.pack()

# Operation selection
label_operation = tk.Label(root, text="Select operation:")
label_operation.pack()
operation_var = tk.StringVar()
operation_var.set("union")
operations = ["union", "intersection", "difference"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

# Perform operation button
button = tk.Button(root, text="Perform Operation", command=perform_operation)
button.pack()

root.mainloop()



# account for univeral set, for complement etc....
# fix code for union
# fix code for difference
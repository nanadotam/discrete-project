# 1.⁠ ⁠Begin by introducing the topic of your course project work.
# 2.⁠ ⁠Define key terms pertinent to your project.
# 3.⁠ ⁠Discuss the methodology employed, explaining code segments and functions in a systematic manner.
# 4.⁠ ⁠Address the testing phase, focusing on edge cases such as atomic scenarios.
# 5.⁠ ⁠Present any propositions derived from your project findings.
# 6.⁠ ⁠Detail strategies for error handling, including scenarios involving incorrect user inputs.
# 7.⁠ ⁠Explore the use of universal symbols or conventions within your project.
# 8.⁠ ⁠Conclude your presentation with a concise summary of key points.
# 9.⁠ ⁠Optionally, include any unique or intriguing aspects of your projects for added interest.


import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

from set_intersection import intersection
from set_union import union
from set_difference import difference
from set_complement import complement

def perform_operation():
    operation = operation_var.get()
    set1 = set(text_entry1.get().split())
    set2 = set(text_entry2.get().split())
    universal_set = set(text_entry_universal.get().split())

    if operation == 'Union':
        result_set = union(set1, set2)
    elif operation == 'Intersection':
        result_set = intersection(set1, set2)
    elif operation == 'Difference':
        result_set = difference(set1, set2)
    elif operation == 'Complement':
        result_set = complement(set1, universal_set)
    
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

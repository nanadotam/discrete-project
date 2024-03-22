from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# Define the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Create a venn diagram
venn2([set1, set2], ('Set 1', 'Set 2'))

# Add a title
plt.title("Venn Diagram")

# Show the plot
plt.show()
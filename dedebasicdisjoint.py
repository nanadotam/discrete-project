import matplotlib.pyplot as plt 
from matplotlib_venn import venn3

cir1 = {1, 2}
cir2 = {3, 4}
cir3 = {5, 6}

# create Venn diagram
venn3([cir1, cir2, cir3], ('cir1', 'cir2'), set_colors=("blue", "pink", "white"))

# display the diagram
plt.show()
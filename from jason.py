import matplotlib.pyplot as plt
from matplotlib_venn import venn2


def plot_sets_venn(set1, set2):
    # Convert sets to set objects
    set1 = set(set1)
    set2 = set(set2)

    # Check if sets are disjoint
    if set1.isdisjoint(set2):
        # Create Venn diagram with no intersection
        venn = venn2(subsets=(len(set1), len(set2), 0),
                     set_labels=('Set A', 'Set B'))

        # Add labels for individual sets
        venn.get_label_by_id('10').set_text('\n'.join(map(str, set1)))
        venn.get_label_by_id('01').set_text('\n'.join(map(str, set2)))
    else:
        # Calculate the intersection and differences
        intersection = set1.intersection(set2)
        only_set1 = set1 - set2
        only_set2 = set2 - set1

        # Create the Venn diagram
        venn = venn2(subsets=(len(only_set1), len(only_set2), len(intersection)),
                     set_labels=('Set 1', 'Set 2'))

        # Add labels for individual sets
        if only_set1:
            venn.get_label_by_id('10').set_text('\n'.join(map(str, only_set1)))
        else:
            venn.get_label_by_id('10').set_text('y')

        if only_set2:
            venn.get_label_by_id('01').set_text('\n'.join(map(str, only_set2)))
        else:
            venn.get_label_by_id('01').set_text('')

        if intersection:
            venn.get_label_by_id('11').set_text('\n'.join(map(str, intersection)))
        else:
            venn.get_label_by_id('11').set_text('')

    plt.title('Venn Diagram of Two Sets A and B')
    plt.show()


# Example sets
set1 = [1, 2, 3, 4, 5, 6]
set2 = [4, 5, 6]

plot_sets_venn(set1, set2)

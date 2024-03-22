import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

from set_intersection import intersection
from set_union import union
from set_difference import difference
from set_complement import complement

def perform_operation():
    opearation = opearation_var.get()

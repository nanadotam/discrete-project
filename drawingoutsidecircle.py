import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2_unweighted, venn3_unweighted
A = set([9,3,6])
B = set([2,4,6,8])
C = set([0,5,1,7])
v = venn3([A,B,C], ('P', 'Q', 'U'))

v.get_label_by_id('100').set_text('\n'.join(map(str,A-B)))
v.get_label_by_id('110').set_text('\n'.join(map(str,A&B)))
v.get_label_by_id('010').set_text('\n'.join(map(str,B-A)))
v.get_label_by_id('001').set_text('\n'.join(map(str,C)))
v.get_patch_by_id('001').set_color('white')
# plt.axis('on')
plt.show()
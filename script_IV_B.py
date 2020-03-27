import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#winter semester
ax.broken_barh([(0, 144)], (40, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(72, 41.5, '1/10-22/2\nwinter semester', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(1, 117), (118,1), (119, 10), (138,6)], (32, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(59.5, 33.5, '2/10-27/01\nclasses', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(120.5, 36, '28/1\nlanguage exams', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(122, 30.67, '28/1-8/2\nexam\nsession', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(147, 30.67, '17/2-22/2\n2nd exam\nsession', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(83,14), (131,7)], (24, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(90, 28, '23/12-6/1\nwinter holidays', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(134.5, 28, '10/2-16/2\nwinter break', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(61, 29), (109, 1)], (16, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(77, 20, '1/12-30/12\n1st registration', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(109.5, 15, '17/1\nresignation deadline', size=5, horizontalalignment='center',
             verticalalignment='center')


#summer semester
ax.broken_barh([(146, 219)], (40, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(255.5, 41.5, '24/2-30/9\nsummer semester', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(146, 107),(258,1), (259, 11), (335,13)], (32, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(199.5, 33.5, '24/2-10/6\nclasses', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(258.5, 31, '15/6\nlanguage exams', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(264, 36, '15/6-27/6\nexam session', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(342.5, 36, '31/8-12/9\n2nd exam session', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(191, 6), (221, 2), (272, 63), (351,15)], (24, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(194, 28, '9/4-14/4\nspring break', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(222, 23, '8/5-9/5\nstudent carnival', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(303.5, 25.5, '29/6-30/8\nsummer holidays', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(358.5, 28, '14/9-30/9\nindividual decisions', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(244, 1), (244, 30)], (16, 3),
               edgecolor=((0, 0, 0, 1)), facecolors=((1, 1, 1, 1)), zorder=3)
plt.text(244.5, 15, '1/6\nresignation deadline', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(259, 20, '1/6-30/6\n1st registration', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.set_ylim(13, 46)
ax.set_xlim(-20, 390)
ax.set_title('2019/20 MIMUW Academic Year', size=10)
ax.set_yticks([])
months = [0, 32, 61, 91, 122, 152, 182, 213, 243, 274, 304, 336, 366]
ax.set_xticks(months)
labels = ['Oct 2019', 'Noc 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020',
          'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020',
          'Aug 2020', 'Sep 2020', 'Oct 2020']
ax.set_xticklabels(labels)
ax.grid(True, zorder=0)

plt.xticks(rotation=45, size=5)
plt.tight_layout()
plt.savefig('plots/IV/IV_B.png', dpi=400)
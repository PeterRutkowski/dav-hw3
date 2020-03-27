import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#winter semester
ax.broken_barh([(0, 144)], (40, 3), alpha=0.6, facecolors=('tab:blue'))
plt.text(72, 41.5, '1/10-22/2\nwinter semester', size=5, horizontalalignment='center',
             verticalalignment='center')

ax.broken_barh([(1, 117), (118, 11), (138,6)], (32, 3), alpha=0.6,
               facecolors=('tab:blue', 'tab:orange', 'tab:blue'))
plt.text(59.5, 33.5, '2/10-27/01\nclasses', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(123.5, 36, '28/1-8/2\nexam session', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(141, 31, '28/1-8/2\n2nd exam session', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(83,14), (131,7)], (24, 3), alpha=0.6, facecolors=('tab:orange', 'tab:blue'))
plt.text(90, 28, '23/12-6/1\nwinter holidays', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(134.5, 28, '10/2-16/2\nwinter break', size=5, horizontalalignment='center',
             verticalalignment='center')


ax.broken_barh([(62, 30), (109, 1), (120,1)], (16, 3), alpha=0.6,
               facecolors=('tab:blue', 'tab:orange', 'tab:blue', 'tab:orange'))
plt.text(77, 20, '1/12-30/12\n1st registration', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(109.5, 15, '17/1\nresignation deadline', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(120.5, 20, '17/1\nlanguage exams', size=5, horizontalalignment='center',
             verticalalignment='center')

ax.broken_barh([], (8,3), alpha=0.6, facecolors=('tab:blue'))




#summer semester

ax.broken_barh([(146, 219)], (40, 3), alpha=0.6, facecolors=('tab:olive'))
plt.text(255.5, 41.5, '24/2-30/9\nsummer semester', size=5, horizontalalignment='center',
             verticalalignment='center')

ax.broken_barh([(146, 107), (272, 63), (351,14)], (32, 3), alpha=0.6,
               facecolors=('tab:olive', 'tab:red', 'tab:olive'))
plt.text(199.5, 33.5, '24/2-10/6\nclasses', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(303.5, 33.5, '29/6-30/8\nsummer holidays', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(358.5, 36, '14/9-30/9\nindividual decisions', size=5, horizontalalignment='center',
             verticalalignment='center')

ax.broken_barh([(258, 12), (336,13)], (24, 3), alpha=0.6, facecolors=('tab:olive', 'tab:olive'))
plt.text(264, 28, '15/6-27/6\nexam session', size=5, horizontalalignment='center',
             verticalalignment='center')
plt.text(342.5, 28, '15/6-27/6\n2nd exam session', size=5, horizontalalignment='center',
             verticalalignment='center')

ax.broken_barh([(191, 6), (221, 2), (244, 30)], (16, 3), alpha=0.6, facecolors=('tab:olive', 'tab:red', 'tab:olive'))

ax.broken_barh([(244, 1), (258,1)], (8,3), alpha=0.6, facecolors=('tab:olive', 'tab:red'))


ax.set_ylim(0, 45)
ax.set_xlim(-20, 390)
ax.set_title('2019/20 MIMUW Academic Year')
ax.set_yticks([15, 25])
ax.set_yticks([])
ax.grid(True)

plt.savefig('plots/IV/IV_color.png', dpi=200)
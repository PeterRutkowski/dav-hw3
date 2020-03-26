import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import animation, rc
#!brew install imagemagick

# import data
data = pd.read_csv("data/data_I_B.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

# country area in km2
country_area = [619745, 42933, 49035, 245857, 1106]

# equivalent to rcParams['animation.html'] = 'html5'
rc('animation', html='html5')

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_ylabel('Population [million]')
ax.set_xlim((1955, 2025))
ax.set_ylim((2000000, 13000000))
ax.set_xticks(np.arange(start=1960,stop=2021, step=10))
ax.set_yticks(np.arange(start=0, stop=13.5, step=1.5)*1000000)

bubble, = ax.scatter([], [], s=[], c=[], alpha=0.5)

# initialization function: plot the background of each frame
def init():
    bubble.set_data([], [], [], [])
    return (bubble,)



# animation function. This is called sequentially
def animate(i):
    time, population, density = [], [], []

    for j in range(5):
        time.append(1960 + i)
        population.append(data[j][i])
        density.append(population[j]/country_area[j])

    density = np.multiply(density, 3)
    colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']

    #plt.text(1975.0, 11500000.0, str(time[0]), size=30,
    #         ha="right", va="top",
    #         bbox=dict(boxstyle="square",
    #                   ec=(1.0, 1.0, 1.0),
    #                   fc=(1.0, 1.0, 1.0),
    #                   )
    #         )

    #for i in range(len(population)):
    #    plt.text(time[i] - 1.77, population[i] - 180000, labels[i])


    time, population, density = [], [], []

    bubble.set_data(time, population, s=density, c=colors)

    return (line,)


# call the animator. blit=True means only re-draw the parts that
# have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=59, interval=500, blit=True)

anim.save('plots/final/II_B.gif', writer='imagemagick', fps=10)
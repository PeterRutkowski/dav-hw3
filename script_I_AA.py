import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data
data = pd.read_csv("data/data_I_A.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

# most populous countries in 1960
# ascending order in terms of population

def plot(population, labels, year, colors):
    # build the plot
    fig, ax = plt.subplots()

    index = np.arange(len(labels))
    index_y = np.arange(8)*200000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i)*0.2,1))

    plt.text(0.75, 1350000000.0, str(year), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1., 0.5, 0.5),
                       fc=(1., 0.8, 0.8),
                       )
             )


    bars = plt.bar(index, population, color=colors)

    for i in range(len(bars)):
        yval = bars[i].get_height()
        plt.text(bars[i].get_x()+0.25, yval + 30000000, labels[i])

    plt.ylabel('Population [billion]')
    plt.xticks([])
    plt.title('The evolution of populations of most populous countries in 1960')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 1500000000)
    plt.tight_layout()
    plt.savefig('I_AA/' + str(year)  + '.png', dpi=150)
    plt.close(fig)

# sorting plot bars in ascending order
colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']

last_index = len(data[0]) - 1
last_input = []
for i in range(5):
    last_input.append(data[i][58])

indices = [] # order of bars in the plot
indices = np.argsort(last_input)

sorted_pop = []
sorted_lab = []
sorted_col = []

for i in range(len(indices)):
    sorted_lab.append(labels[indices[i]])
    sorted_col.append(colors[indices[i]])

population = []

for i in range(59):
    for j in range(5):
        population.append(data[j][i])
    for k in range(len(indices)):
        sorted_pop.append(population[indices[k]])

    plot(sorted_pop, sorted_lab, i+1960, sorted_col)

    population = []
    sorted_pop = []
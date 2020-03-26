import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# most populous countries in 1960 in terms of population

# import data
data = pd.read_csv("data/data_I_A.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

# country area in km2
country_area = [9597000, 3287000, 9834000, 17100000, 377915]

def plot(data, labels, year_bound):
    fig, ax = plt.subplots()

    colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']
    time, population = [], []

    for i in range(0,year_bound + 1):
        time = np.arange(start=1960,stop=1960+i+1,step=1)

        for j in range(0,1+i):
            population.append(data[:,j])
        population = np.swapaxes(population, 0, 1)

        for j in range(len(labels)):
            ax.plot(time, population[j], label=labels[j], color=colors[j])
            if i == year_bound:
                plt.text(1960.5 + year_bound, population[j][i] - 20000000, labels[j])

        time, population = [], []

    index_y = np.arange(8) * 200000000
    labels_y = []
    for i in range(len(index_y)):
        labels_y.append(np.round((i) * 0.2, 1))

    plt.text(1977.0, 1350000000.0, str(1960 + year_bound), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1.0, 1.0, 1.0),
                       fc=(1.0, 1.0, 1.0),
                       )
             )

    plt.ylabel('Population [billion]')
    plt.xticks(np.arange(start=1960,stop=2021,step=10))
    plt.title('The evolution of populations of most populous countries in 1960')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 1500000000)
    plt.xlim(1960, 2023)
    #plt.tight_layout()

    plt.savefig('plots/II_A/' + str(1960 + year_bound) + '.png', dpi=200)
    plt.close()

for i in range(59):
    plot(data, labels, i)
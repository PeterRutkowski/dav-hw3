import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Balkan war population evolution

# import data
data = pd.read_csv("data/data_III.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

def plot(population, labels, year):
    # build the plot
    fig, ax = plt.subplots()

    index = np.arange(len(labels))
    index_y = np.arange(0,7000000,1500000)
    labels_y = np.arange(0,9,1.5)

    plt.text(0.75, 5900000.0, str(year), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1.0, 1.0, 1.0),
                       fc=(1.0, 1.0, 1.0),
                       )
             )

    if year > 1990 and year < 2002:
        plt.text(0.22, 0.75, 'Yugoslav Wars', size=20, horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)

    colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']

    bars = plt.bar(index, population, color=colors)

    for i in range(len(bars)):
        yval = bars[i].get_height()
        if yval > 0:
            plt.text(bars[i].get_x()+0.25, yval + 100000, labels[i])

    plt.ylabel('Population [million]')
    plt.xticks([])
    plt.title('The evolution of populations of Balkan countries 1960-2018')
    plt.yticks(index_y, labels_y)
    plt.ylim(0, 6500000)
    plt.tight_layout()
    if year > 1990 and year < 2002:
        plt.savefig('plots/III/' + str(year)  + '_1.png', dpi=200)
        plt.savefig('plots/III/' + str(year) + '_2.png', dpi=200)
        plt.savefig('plots/III/' + str(year) + '_3.png', dpi=200)
        plt.savefig('plots/III/' + str(year) + '_4.png', dpi=200)
    else:
        plt.savefig('plots/III/' + str(year) + '.png', dpi=200)
    plt.close(fig)

population = []
for i in range(59):
    population = data[:,i]
    plot(population, labels, 1960 + i)
    population = []
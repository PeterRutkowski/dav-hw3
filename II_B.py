import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data
data = pd.read_csv("data/data_I_B.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

# country area in km2
country_area = [619745, 42933, 49035, 245857, 1106]

time = []
population = []
density = []

def plot(time, population, density, labels):
    colors = ['dodgerblue', 'orchid', 'green', 'darkorange', 'brown']
    plt.scatter(time, population, s=density, alpha=0.5, c=colors)

    plt.text(1975.0, 11500000.0, str(time[0]), size=30,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1.0, 1.0, 1.0),
                       fc=(1.0, 1.0, 1.0),
                       )
             )


    for i in range(len(population)):
        plt.text(time[i] - 1.77, population[i] - 180000, labels[i])
    plt.ylabel('Population [million]')
    plt.ylim(2000000, 13000000)
    plt.xlim(1955, 2025)
    plt.xticks(np.arange(start=1960,stop=2021, step=10))
    plt.yticks(np.arange(start=0, stop=13.5, step=1.5)*1000000, np.arange(start=0, stop=13.5, step=1.5))
    plt.savefig('plots/II_B/' + str(time[0]) + '.png', dpi=200)
    plt.clf()
    return

gif = []

for i in range(59):
    for j in range(5):
        time.append(1960 + i)
        population.append(data[j][i])
        density.append(population[j]/country_area[j])

    density = np.multiply(density, 3)
    plot(time, population, density, labels)

    time = []
    population = []
    density = []
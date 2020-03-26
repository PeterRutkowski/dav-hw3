import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# countries closest to Poland in 1971 in terms of population

# import data
data = pd.read_csv("data/data_I_C.csv")
labels = np.asarray(data['country'])
data = np.asarray(data.drop(['country'], axis=1))

for i in range(0,59):
    population = data[:,i]
    fig, ax = plt.subplots()

    ax.pie(population, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    plt.text(0.05, 0.53, str(1960 + i), size=23, horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes,
             ha="right", va="top",
             bbox=dict(boxstyle="square",
                       ec=(1.0, 1.0, 1.0),
                       fc=(1.0, 1.0, 1.0),
                       )
             )
    plt.text(0.5 , 1.055, 'The evolution of the distribution of populations\n' +
              'of countries that were most similar population-wise\n' +
              'to Poland in 1971', size=13, horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes)

    plt.savefig('plots/II_C/' + str(1960 + i) + '.png', dpi=200)
    plt.close(fig)
    plt.tight_layout()
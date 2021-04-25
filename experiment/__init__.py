import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def second_layer_t():
    data = pd.read_csv("experiment/t2.csv")
    sns.lineplot(x='t2', y='ndi', data=data)
    plt.show()


def first_layer_k(y='1dse'):
    data = pd.read_csv("experiment/h1k2.csv")
    sns.lineplot(x='k', y=y, data=data)
    # sns.lineplot(x='k', y='2dse', data=data)
    plt.show()

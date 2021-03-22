import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def second_layer_t():
    data = pd.read_csv("experiment/t2.csv")
    sns.lineplot(x='t2', y='ndi', data=data)
    plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def first_layer_t(y='1dse'):
    """
    第一层t
    :param y:
    :return:
    """
    data = pd.read_csv("experiment/t1_half.csv")
    sns.lineplot(x='t1', y=y, data=data)
    plt.show()


def dux_1l():
    data = pd.read_csv("experiment/t1_half.csv")
    x = data.get('t1')
    y = data.get('1dse')
    du = []
    for i in range(len(x) - 1):
        du.append((y.get(i + 1) - y.get(i)) / (x.get(i + 1) - x.get
        (i)))
    du.append(0.001)
    plt.plot(x, du)
    plt.show()
    print(du)


def second_layer_t(y='compressing ratio'):
    data = pd.read_csv("experiment/bf_t2_ndi.csv")
    sns.lineplot(x='t2', y=y, data=data)
    plt.show()


def first_layer_k(y='1dse'):
    data = pd.read_csv("experiment/h1k2.csv")
    sns.lineplot(x='k', y=y, data=data)
    # sns.lineplot(x='k', y='2dse', data=data)
    plt.show()


def second_layer(path, x='k', y='1dse'):
    data = pd.read_csv(path)
    sns.lineplot(x=x, y=y, data=data)
    plt.show()


def find_stable_points(list):
    """
    找到稳定点
    :return:
    """
    res = {}
    for i in range(1, len(list) - 1):
        if list[i - 1] < list[i] and list[i + 1] < list[i]:
            res[i + 1] = list[i]

    return res


def print_sps(path, x):
    """
    打印稳定点
    :param path:
    :param x:
    :return:
    """
    print("find stable points from file {}[{}]".format(path.split('/')[-1], x))
    data = pd.read_csv(path)
    col = data.get(x).values.tolist()
    res = find_stable_points(col)
    if len(res) == 0:
        print("no stable points")
    else:
        print(res)


def show_distribution(x: list, y: list):
    plt.title("distribution of the size of graph result")
    fig = sns.barplot(x, y)

    plt.show()


# 定义函数来显示柱状上的数值
def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2. - 0.25, 1.01 * height, '%s' % int(height))

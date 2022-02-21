import xlrd

from experiment import show_distribution

import matplotlib.pyplot as plt
import pandas as pd

twoD_se_path = "/Users/gem/IdeaProjects/deDoc/2D"
d = {}


def show_2d_distribution():
    try:
        two_dim_result = open(twoD_se_path)
    except Exception as e:
        print(e)

    for line in two_dim_result.readlines():
        comm = line.rstrip().split('\t')
        key = len(comm)
        d[key] = d.get(key, 0) + 1

    x = []
    y = []
    for e in sorted(d):
        x.append(e)
        y.append(d[e])
    show_distribution(x, y)


def box():
    dt = pd.DataFrame({
        "EGB": [3.837045737950657842e-01, 6.898546910670294574e-01, 8.495735583439568694e-01, 7.658396567171686931e-01,
                6.540423152383226801e-01, 7.731490615010176981e-01, 8.155630829460184250e-01, 6.711374598469169728e-01],
        "Kmeans": [5.599461217073560260e-01, 7.076783780797146761e-01, 6.496240009486099476e-01,
                   8.152979166387718246e-01,
                   6.451808113032145853e-01, 8.129271859245589260e-01, 8.375371590287089552e-01,
                   7.700779109997307748e-01],
        "FCM": [5.176270370814823885e-01, 6.363020575956026548e-01, 7.153498082830076488e-01, 6.823182280088725404e-01,
                6.622568353573511368e-01, 8.022155169262452645e-01, 7.928263717150212386e-01, 6.988530350265860225e-01],
        "deIIMG-3D": [5.304453998861654584e-01, 7.270480704925768034e-01, 7.885413783092829476e-01,
                      8.188109489512085393e-01,
                      7.010884614187723463e-01, 8.015790846953382287e-01, 8.603952217248183043e-01,
                      7.318497403453820827e-01]
    })
    plt.boxplot(x=dt.values, labels=dt.columns, whis=1.5)
    plt.show()


def box2():
    dt = pd.DataFrame({
        "EGB": [5.14085563619263, 5.271113606699326937e+00, 6.273064535958352117e+00, 5.133584467604174861e+00,
                3.903701850138709961e+00, 3.475987212562506645e+00, 4.527342268485829990e+00, 6.432475119319809309e+00],
        "Kmeans": [1.714913963367999727e+00, 2.921347864973645958e+00, 3.309405028379860170e+00,
                   3.019743035755567462e+00,
                   2.822365026187219517e+00, 2.460814800275855418e+00, 2.168873026649711822e+00,
                   3.482154698768695766e+00],
        "FCM": [2.037927271655908257e+00, 3.397878151293059368e+00, 4.011398846521490036e+00, 3.692682000306318546e+00,
                3.001668526554142957e+00, 2.569261192909479963e+00, 2.244033649872656078e+00, 3.745287510267380604e+00],
        "deIIMG-3D": [1.965023896580066598e+00, 2.901028321279981448e+00, 3.509913006394726587e+00,
                      2.389114687119496150e+00,
                      2.361444435537439102e+00, 2.121574725329069988e+00, 2.182454209730122496e+00,
                      3.500877388809606749e+00]
    })
    plt.boxplot(x=dt.values, labels=dt.columns, whis=1.5)
    plt.show()


def box3():
    pri = xlrd.open_workbook("/Users/gem/Desktop/毕业论文/数据集/PRI.xls")
    sheet = pri.sheet_by_index(0)
    egb = sheet.col_values(0, 0, 501)
    km = sheet.col_values(1, 0, 501)
    fcm = sheet.col_values(2, 0, 501)
    dei = sheet.col_values(3, 0, 501)

    dt = pd.DataFrame({
        "EGB": egb,
        "Kmeans": km,
        "fcm": fcm,
        "deIIMG-3D": dei
    })
    plt.boxplot(x=dt.values, labels=dt.columns, whis=1.5)
    plt.show()


def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')


def dis1():
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码

    labels = ['0.00-0.49', '0.50-0.59', '0.60-0.69', '0.70-0.79', '0.80-0.89', '0.90-1.00']
    a = [231, 73, 71, 77, 39, 9]
    b = [24, 54, 162, 210, 47, 3]
    c = [27, 57, 195, 203, 17, 1]
    d = [32, 42, 118, 216, 87, 5]
    # labels = ['0.00-0.99', '1.00-1.99', '2.00-2.99', '3.00-3.99', '4.00-6.00']
    # a = [21, 147, 241, 87, 4]
    # b = [3, 27, 178, 211, 81]
    # c = [2, 12, 113, 258, 115]
    # d = [1, 34, 181, 203, 81]

    # marks = ["o", "X", "+", "*", "O"]

    x = np.arange(len(labels))  # 标签位置
    width = 0.15  # 柱状图的宽度

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width * 2, a, width, label='EGB', )
    rects2 = ax.bar(x - width + 0.01, b, width, label='Kmeans')
    rects3 = ax.bar(x + 0.02, c, width, label='FCM', )
    rects4 = ax.bar(x + width + 0.03, d, width, label='deIIMG-3D')

    # 为y轴、标题和x轴等添加一些文本。
    ax.set_ylabel('Number of pics', fontsize=16)
    ax.set_xlabel('PRI', fontsize=16)
    # ax.set_title('不同算法PRI得分分布图')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # autolabel(rects1, ax)
    # autolabel(rects2, ax)
    # autolabel(rects3, ax)
    # autolabel(rects4, ax)

    fig.tight_layout()
    plt.show()

import seg
from experiment import second_layer_t, first_layer_k, second_layer, print_sps, first_layer_t, dux_1l
from seg import Distribution
from seg.Distribution import box, box2, dis1
from seg.GrabCut import grab_cut
from seg.SLIC import SLICProcessor
from seg.kmeans import kmeans_seg
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    input_path = "/Users/gem/PyProject/SE_image_seg/data/horse.jpg"

    # kmeans_seg(5, input_path)
    # grab_cut(input_path)

    # p = SLICProcessor('/Users/gem/PyProject/SE_image_seg/data/fruits.jpg', 200, 40)
    # p.iterate_10times()

    # first_layer_t('compressing ratio')
    # second_layer_t()
    # first_layer_k('')
    # second_layer("experiment/butterfly/bf_h2_1_30.csv", 'k', '1dse')
    # print_sps("experiment/butterfly/bf_1_20_new.csv", '2dse')
    # Distribution.show_2d_distribution()
    # dux_1l()
    # box2()
    # pri = xlrd.open_workbook("/Users/gem/Desktop/毕业论文/数据集/VI.xls")
    # sheet = pri.sheet_by_index(0)
    # egb = sheet.col_values(0, 0, 501)
    # km = sheet.col_values(1, 0, 501)
    # fcm = sheet.col_values(2, 0, 501)
    # dei = sheet.col_values(3, 0, 501)
    #
    # dt = pd.DataFrame({
    #     "EGB": egb,
    #     "Kmeans": km,
    #     "fcm": fcm,
    #     "deIIMG-3D": dei
    # })
    # plt.boxplot(x=dt.values, labels=dt.columns, whis=1.5)
    # plt.show()
    # dis1()

    # seg.seg_csv("/Users/gem/Documents/CV/segmap/val", "segmap9/val/", pt='9')
    # seg.rm_endl("segmap1/test/2018.csv")

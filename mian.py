from experiment import second_layer_t, first_layer_k, second_layer, print_sps, first_layer_t
from seg import Distribution
from seg.GrabCut import grab_cut
from seg.SLIC import SLICProcessor
from seg.kmeans import kmeans_seg

if __name__ == '__main__':
    input_path = "/Users/gem/PyProject/SE_image_seg/data/rboat.jpg"

    # kmeans_seg(1000, input_path)
    # grab_cut(input_path)

    # p = SLICProcessor('/Users/gem/PyProject/SE_image_seg/data/fruits.jpg', 200, 40)
    # p.iterate_10times()

    # first_layer_t('compressing ratio')
    # second_layer_t()
    # first_layer_k('')
    # second_layer("experiment/butterfly/bf_h2_1_30.csv", 'k', '1dse')
    # print_sps("experiment/butterfly/bf_1_20_new.csv", '2dse')
    Distribution.show_2d_distribution()

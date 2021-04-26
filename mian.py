from experiment import second_layer_t, first_layer_k, second_layer
from seg.GrabCut import grab_cut
from seg.SLIC import SLICProcessor
from seg.kmeans import kmeans_seg

if __name__ == '__main__':
    input_path = "/Users/gem/PyProject/SE_image_seg/data/mountain.jpg"

    # kmeans_seg(5, input_path)
    # grab_cut(input_path)

    # p = SLICProcessor('/Users/gem/PyProject/SE_image_seg/data/fruits.jpg', 200, 40)
    # p.iterate_10times()

    # second_layer_t()
    # first_layer_k('2dse')
    second_layer("experiment/horse/h1k.csv", 'k', '2dse')

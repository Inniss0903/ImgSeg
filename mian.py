from seg.GrabCut import grab_cut
from seg.SLIC import SLICProcessor
from seg.kmeans import kmeans_seg

if __name__ == '__main__':
    input_path = "/Users/gem/PyProject/SE_image_seg/data/swan.jpg"

    kmeans_seg(2, input_path)
    # grab_cut(input_path)

    # p = SLICProcessor('/Users/gem/PyProject/SE_image_seg/data/fruits.jpg', 200, 40)
    # p.iterate_10times()


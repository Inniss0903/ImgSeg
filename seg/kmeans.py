import cv2
import matplotlib.pyplot as plt
import numpy as np


def kmeans_seg(k, input_path: str):
    name = input_path.split("/")[-1].split(".")[0]
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    # 变换图像通道bgr->rgb
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])

    # 3个通道展平
    img_flat = img.reshape((img.shape[0] * img.shape[1], 3))
    img_flat = np.float32(img_flat)

    # 迭代参数
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 20, 0.5)
    flags = cv2.KMEANS_RANDOM_CENTERS

    # 聚类,这里k=2
    compactness, labels, centers = cv2.kmeans(img_flat, k, None, criteria, 10, flags)

    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    # 显示结果
    # img_output = labels.reshape((img.shape[0], img.shape[1]))
    img_output = res.reshape((img.shape))
    plt.imsave("Result/{}_km{}.jpg".format(name, k), img_output)
    plt.subplot(121), plt.imshow(img), plt.title('input')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122), plt.imshow(img_output), plt.title('kmeans k={}'.format(k))
    plt.xticks([])
    plt.yticks([])
    plt.show()

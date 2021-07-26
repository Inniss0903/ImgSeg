16.59152116
.89287016
.943778
from scipy import io
import scipy.misc
import scipy
import imageio
import cv2
import os

# 运行时需要改变root值为BSD500所在的相应根目录
root = '/Users/gem/Documents/CV/BSR/BSDS500/'
PATH = os.path.join(root, 'data/groundTruth')

for sub_dir_name in ['train', 'test', 'val']:
    sub_pth = os.path.join(PATH, sub_dir_name)
    # 为生成的图片新建个文件夹保存
    save_pth = os.path.join(root, 'data/GT_1_convert', sub_dir_name)
    os.makedirs(save_pth, exist_ok=True)
    print('开始转换' + sub_dir_name + '文件夹中内容')
    for filename in os.listdir(sub_pth):
        # 读取mat文件中所有数据
        # mat文件里面是以字典形式存储的数据
        # 包括 dict_keys(['__globals__', 'groundTruth', '__header__', '__version__'])
        # 如果要用到'groundTruth']中的轮廓
        # x['groundTruth'][0][0][0][0][1]为轮廓
        # x['groundTruth'][0][0][0][0][0]为分割图
        data = io.loadmat(os.path.join(sub_pth, filename))
        seg_data = data['groundTruth'][0][0][0][0][1]
        # 存储的是归一化后的数据：0<x<1
        # 因此需要还原回0<x<255
        # seg_image = cv2.cvtColor(seg_data, cv2.COLOR_GRAY2BGR)
        seg_data_255 = seg_data * 4
        seg_data_255 = seg_data_255.astype(int)
        new_img_name = filename.split('.')[0] + '.jpg'
        print(new_img_name)
        # scipy.misc.imsave(os.path.join(save_pth, new_img_name), seg_data_255)  # 保存图片
        imageio.imwrite(os.path.join(save_pth, new_img_name), seg_data_255)
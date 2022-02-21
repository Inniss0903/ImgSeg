import os

import numpy as np
import pandas as pd


def rm_endl(file):
    f = open(file, 'rb+')
    m = 1
    f.seek(-m, os.SEEK_END)
    lines = f.readlines()
    f.seek(-len(lines[-1]), os.SEEK_END)
    f.truncate()
    f.close()


def seg_csv(src_path, dst_path, pt='1'):
    for root, dirs, files in os.walk(src_path):
        for file in files:
            f_spl = file.split('_')
            if f_spl[1] == pt:
                txt = np.loadtxt(root + "/" + file, dtype=int)
                pdtxt = pd.DataFrame(txt)
                pdtxt.to_csv(dst_path + f_spl[0] + ".csv", index=False, header=False)

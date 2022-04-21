#ヒストグラム
#参考文献
#http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html

import numpy as np
import cv2
from matplotlib import pyplot as plt     #ヒストグラムを描写するためのモジュール


img1 = cv2.imread('money1.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.savefig("plt1.png")     #ヒストグラムの保存
plt.show()

img2 = cv2.imread('animal.jpeg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img2],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.savefig("plt2.png")     #ヒストグラムの保存
plt.show()
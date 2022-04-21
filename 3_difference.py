#差分画像作成
#参考文献
#https://www.higashisalary.com/entry/opencv-diff-pic


import numpy as np
import cv2

#画像の読み込み
img1=cv2.imread("sample1.png",cv2.IMREAD_GRAYSCALE)
img1=img1.astype(np.float32)
img2=cv2.imread("sample2.png",cv2.IMREAD_GRAYSCALE)
img2=img2.astype(np.float32)

#輝度差し引き
img3=img1-img2
img3=np.where(img3<0,0,img3)
img3=img3.astype(np.uint8)

#画像出力
cv2.imshow("sabun.png", img3)

#画像保存
cv2.imwrite("sabun.png", img3)
cv2.waitKey(0)

#全ての画像のウィンドウを閉じる
cv2.destroyAllWindows()
#画像処理_特徴抽出_AKAZE
#参考文献
#https://python-debut.blogspot.com/2020/02/blog-post_24.html


import numpy as np
import cv2

img = cv2.imread('dog.jpg')

#特徴抽出するための箱を作る．
akaze = cv2.AKAZE_create()    #AKAZE

#読み込んだ画像の特徴検出
kp_akaze = akaze.detect(img)

#画像への特徴点の書き込み
img_akaze = cv2.drawKeypoints(img, kp_akaze, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('img_akaze.png', img_akaze)
cv2.imshow('img_akaze.png', img_akaze)
cv2.waitKey(0)

cv2.destroyAllWindows()
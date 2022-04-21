#画像処理_特徴抽出_ORB
#参考文献
#https://python-debut.blogspot.com/2020/02/blog-post_24.html


import numpy as np
import cv2

img = cv2.imread('dog.jpg')

#特徴抽出するための箱を作る．
orb =  cv2.ORB_create()       #ORB


#読み込んだ画像の特徴検出
kp_orb = orb.detect(img)

#画像への特徴点の書き込み
img_orb = cv2.drawKeypoints(img, kp_orb, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('img_orb.png', img_orb)
cv2.imshow('img_orb.png', img_orb)
cv2.waitKey(0)

cv2.destroyAllWindows()
#画像処理_SURF
#参考文献
#https://python-debut.blogspot.com/2020/02/blog-post_24.html
#https://stackoverflow.com/questions/52305578/sift-cv2-xfeatures2d-sift-create-not-working-even-though-have-contrib-instal
#opencvのバージョンを下げた

import numpy as np
import cv2

img = cv2.imread('dog.jpg')

#特徴抽出するための箱を作る．
surf = cv2.xfeatures2d.SURF_create()  #SURF


#読み込んだ画像の特徴検出
kp_surf = surf.detect(img)

#画像への特徴点の書き込み
img_surf = cv2.drawKeypoints(img, kp_surf, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('img_surf.png', img_surf)

#opencvのバージョンを下げたため，以下の関数が使えなかった．
#cv2.imshow('img_surf.png', img_surf)
#cv2.waitKey(0)

#cv2.destroyAllWindows()
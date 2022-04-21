#画像マッチング
#参考文献
#https://wonderfuru.com/opencv%E3%81%A7%E7%94%BB%E5%83%8F%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E3%82%92%E3%81%99%E3%82%8B/


import numpy
import cv2

img1 = cv2.imread('cup1.JPG')
img2 = cv2.imread('cup2.JPG')
h,w,_ = img1.shape
rate = int(max(h,w)/512)

# 画像サイズを最大512に変更
img1 = cv2.resize(img1, (int(w/rate), int(h/rate)))
img2 = cv2.resize(img2, (int(w/rate), int(h/rate)))

#特徴点抽出のための検出器作成
detector = cv2.ORB_create()

# 特徴点抽出
kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)

#BFMatcher型オブジェクト作成
bf = cv2.BFMatcher()

# マッチング
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# 画像書き出し、出力
out = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
cv2.imwrite('matching.png', out)
cv2.imshow('matching.png', out)
cv2.waitKey(0)

cv2.destroyAllWindows()
#画像の表示，縮小拡大，回転，二値化
#参考文献
#https://dev.classmethod.jp/articles/open-and-close-an-image-in-a-window-in-opencv/
#https://qiita.com/kenfukaya/items/dfa548309c301c7087c4
#https://note.nkmk.me/python-opencv-numpy-rotate-flip/
#https://www.delftstack.com/ja/howto/python/opencv-rotate-image/
#https://qiita.com/tokkuri/items/ad5e858cbff8159829e9


import numpy as np
import cv2

#画像表示
img = cv2.imread("sample.png")
cv2.imshow("color",img)
cv2.waitKey(0)            #画像を表示しているウィンドウ上で何かキーを押さないと次の処理に移らない

#高さ・幅の定義
height = img.shape[0]     #画像の高さをheightに格納
width = img.shape[1]      #画像の幅をwidthに格納　　2ついっぺんにやるなら，(height, width) = img.shape[:2]

#画像縮小（0.5倍）
img2 = cv2.resize(img , (int(width*0.5), int(height*0.5)))
cv2.imshow("samll",img2)
cv2.waitKey(0)

#画像拡大（1.5倍）
img3 = cv2.resize(img , (int(width*1.5), int(height*1.5)))
cv2.imshow("big",img3)
cv2.waitKey(0)

#画像回転（90度回転）
img4 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("kaiten90",img4)
cv2.waitKey(0)

#画像回転(任意の角度)
center = (int(width/2), int(height/2))  #画像の中心を計算
angle = 45                              #画像の回転角度を定義
scale = 1                               #画像のスケールを定義
rotated = cv2.getRotationMatrix2D(center, angle, scale)
img5 = cv2.warpAffine(img, rotated, (width, height))
cv2.imshow("ninikaiten",img5)
cv2.waitKey(0)

#画像二値化
img0 = cv2.imread("sample.png", 0)     #画像をグレースケールで読み込む
threshold = 128                         #閾値の定義(この値によって白か黒かを分ける)
ret, img_thresh = cv2.threshold(img0, threshold, 255, cv2.THRESH_BINARY)    #閾値128を超えた画素を255にしている
cv2.imshow("img_thresh", img_thresh)
cv2.waitKey(0)

#全ての画像のウィンドウを閉じる
cv2.destroyAllWindows()
import cv2
import numpy as np



img_rgb=cv2.imread('otlar.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)


nesne=cv2.imread('zararli_ot.jpg',0) 

w,h=nesne.shape[::-1] 

res=cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED) 
threshold=0.90

loc=np.where(res>threshold) 

for n in zip(*loc[::-1]): 
    cv2.rectangle(img_rgb,n,(n[0]+w,n[1]+h),(0,255,0),2) 
    cv2.putText(img_rgb,"bitki",(n[0]+w,n[1]+h),cv2.QT_FONT_NORMAL,3, (255,255,255),1)


cv2.imshow('cikti',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

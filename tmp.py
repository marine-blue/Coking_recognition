import cv2

img = cv2.imread("./spectrogram/train/cutting/board00.png")
print(img)
cv2.imshow('aaa.png',img)
cv2.waitKey(0)
img = cv2.resize(img,(244,244))

cv2.imshow('aaa.png',img)
cv2.waitKey(0)
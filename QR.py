
'''
import qrcode

img = qrcode.make("https://www.youtube.com")
img.save("bitcoin.png")

qrcode.make("Baby yoda ate 20 biscuits today")
img.save("google.png")

import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("google.png"))
print(val)
'''
# This code show QR code

import cv2

img = cv2.imread('google.png', -1)

#print(img)

cv2.imshow('image', img)
k = cv2.waitkey(0) & 0xFF

if k == 27:
    cv2.destroyAllwindows()
elif k == ord('s'):
    cv2.imwrite('youtube.png', img)
    cv2.destroyAllwindows()












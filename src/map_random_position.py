import cv2
import random

img = cv2.imread('map.jpg', cv2.IMREAD_COLOR)

width = img.shape[1]
height = img.shape[0]


print('width : ' + str(width) + ', height : ' + str(height))

w_position = 0
h_position = 0

while w_position is 0 and h_position is 0:
    w_position = random.randrange(1, width)
    h_position = random.randrange(1, height)
    print('width postion : ' + str(w_position) + ', h position : ' + str(h_position))

    bgr = img[h_position, w_position]
    print('bgr : ' + str(bgr))

    if bgr[2] <= 200 and bgr[1] <= 200:
        w_position = 0
        h_position = 0

# img, start position, end position, color(bgr), thickness
cv2.line(img, (w_position, 0), (w_position, height), (0, 0, 255), 1)
cv2.line(img, (0, h_position), (width, h_position), (0, 0, 255), 1)

cv2.imshow('map', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



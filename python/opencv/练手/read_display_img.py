import cv2 as cv
img = cv.imread("D://test.jpg",1)

cv.namedWindow("Image")

cv.imshow("Image", img)
cv.waitKey()

cv.destroyAllWindows()
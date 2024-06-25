import cv2

img = cv2.imread("Projects/img.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Miraj", img)
cv2.waitKey(0)

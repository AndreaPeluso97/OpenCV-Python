import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
h,w= image.shape[:2]
cv2.imshow("image",image)
cv2.waitKey()

M = np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Shifted down and right", shifted)
cv2.waitKey()

M = np.float32([[1,0,-50],[0,1,-90]])
shifted = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Shifted top and left", shifted)
cv2.waitKey()

def tranlate(image, x,y):
    h,w = image.shape[:2]
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image, M, (w,h))

    return shifted

shifted = tranlate(image, x=0, y=100)
cv2.imshow("Shifting with custom function", shifted)
cv2.waitKey()


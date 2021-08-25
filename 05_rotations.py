import argparse
import cv2
from numpy import rot90

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
h,w= image.shape[:2]
center= (w//2, h//2)
cv2.imshow("image",image)
cv2.waitKey()

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("rotated by 45 degrees", rotated)
cv2.waitKey()

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("rotated by 90 degrees", rotated)
cv2.waitKey()

def rotate(image, angle, center=None, scale=1.0):
    h,w = image.shape[:2]
    
    if center is None:
        center = (w//2,h//2)
        
    M = cv2.getRotationMatrix2D(center, angle, scale)
     
    rotated = cv2.warpAffine(image, M, (w,h))
     
    return rotated   

rotated = rotate(image, 45)
cv2.imshow("Rotated by 45 degrees with our function", rotated)
cv2.waitKey()

#cv2.ROTATE_90_CLOCKWISE | CV2.ROTATE_90_COUNTERCLOCKWISE | cv2.ROTATE_120 
rotated= cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Roated by 180 degrees", rotated)
cv2.waitKey()
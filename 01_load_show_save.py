import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], cv2.IMREAD_COLOR)

print("image.shape: {}".format(image.shape))
print("image.shape: {}".format(image.dtype))

print("width: {}".format(image.shape[1]))
print("height: {}".format(image.shape[0]))

cv2.imshow("image", image)
cv2.waitKey()

cv2.imwrite("out/01_image.jpg", image)


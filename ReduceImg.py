import cv2
import numpy as np

image_read = cv2.imread('1.jpg',0) 
original_image = np.asarray(image_read)
width , height = 452,452
resize_image = np.zeros(shape=(width,height))

for W in range(width):
    for H in range(height):
        new_width = int( W * original_image.shape[0] / width )
        new_height = int( H * original_image.shape[1] / height )
        resize_image[W][H] = original_image[new_width][new_height]

print("Resized image size : " , resize_image.shape)

cv2.imshow(resize_image)
cv2.waitKey(0)
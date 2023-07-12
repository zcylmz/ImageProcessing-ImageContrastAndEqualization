""""""

import cv2


# Load the input image in BGR format
img = cv2.imread('image_1.jpg')

# Convert the input image from BGR to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold the image to get only red colors
mask_red = cv2.inRange(img_hsv, (0, 70, 50), (10, 255, 255))
mask_red2 = cv2.inRange(img_hsv, (170, 70, 50), (180, 255, 255))
mask_red = cv2.bitwise_or(mask_red, mask_red2)

# Convert the mask to grayscale
mask_gray = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)

# Convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Apply the mask to the original image
img_red = cv2.bitwise_and(img, mask_gray)

# Apply the inverted mask to the grayscale image
img_gray = cv2.bitwise_and(gray, cv2.bitwise_not(mask_gray))

# Combine the red and grayscale images
img_result = cv2.add(img_red, img_gray)

# Display the resulting image
cv2.imshow('Red Objects Highlighted', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()




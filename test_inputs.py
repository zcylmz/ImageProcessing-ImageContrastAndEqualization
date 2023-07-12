import cv2
import numpy as np


# Define a function to apply red highlight and grayscale to an image
def highlight_red_and_gray(img):
    # Convert image to YIQ color space
    img_yiq = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold to extract red regions
    mask = cv2.inRange(img_yiq, np.array([0, 0, 120]), np.array([255, 120, 255]))

    # Invert mask to extract non-red regions
    mask_inv = cv2.bitwise_not(mask)

    # Convert non-red regions to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply red mask to original image
    img_red = cv2.bitwise_and(img, img, mask=mask)

    # Apply inverted mask to grayscale image
    img_bg = cv2.bitwise_and(img_gray, img_gray, mask=mask_inv)

    # Merge red and gray images
    img_out = cv2.add(img_red, cv2.cvtColor(img_bg, cv2.COLOR_GRAY2BGR))

    return img_out


# Test the function with different input images
img1 = cv2.imread("test_image.jpg")
out1 = highlight_red_and_gray(img1)
cv2.imshow("Test 1", out1)

#
# img2 = cv2.imread("test2.jpg")
# out2 = highlight_red_and_gray(img2)
# cv2.imshow("Test 2", out2)

cv2.waitKey(0)
cv2.destroyAllWindows()

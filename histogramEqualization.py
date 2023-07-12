
import cv2


# Load the input image in BGR format
img = cv2.imread('image_1.jpg')

# Convert the input image from BGR to YIQ color space
img_yiq = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split the YIQ image into separate channels
y, cr, cb = cv2.split(img_yiq)

# Apply histogram equalization to the Y channel
y_eq = cv2.equalizeHist(y)

# Merge the equalized Y channel with the Cr and Cb channels
img_yiq_eq = cv2.merge((y_eq, cr, cb))

# Convert the merged YIQ image back to the BGR color space
img_result = cv2.cvtColor(img_yiq_eq, cv2.COLOR_YCrCb2BGR)

# Display the resulting image
cv2.imshow('Histogram Equalized Image', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


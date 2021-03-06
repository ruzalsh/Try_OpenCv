import cv2
import numpy as np

image = cv2.imread('../images/dog.jpg')
height, width = image.shape[:2]

#pixel cordinates
start_row, start_col = int(height * .25), int(width * .25)
end_row, end_col = int(height * .75), int(width * .75)

# using numpy indexing to crop the rectangle of the image
cropped = image[start_row:end_row,start_col:end_col]

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
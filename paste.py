from PIL import Image
import cv2
import numpy as np
import imutils
from imutils import paths

array = []
for x in range(3):
    im = cv2.imread('ROI_' +str(x) + ".jpeg")
    array.append(im)
array.append('ROI_4.jpeg')
sticher = cv2.Stitcher_create(0)
rotated3 = cv2.rotate(array[0],cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated4 = cv2.rotate(array[1],cv2.ROTATE_180)
cv2.imwrite('3.png',rotated3)
cv2.imwrite('4.png',rotated4)
(status, stitched) = sticher.stitch([rotated4,rotated3])
if status == 0:
	# write the output stitched image to disk
	cv2.imwrite('test.png', stitched)
	# display the output stitched image to our screen
# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))
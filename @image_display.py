import numpy as np
import cv2

input1 = cv2.imread(r'C:\Users\lenovo\Desktop\Horse\Horse.jpg')
cv2.imshow('Horse', input1)
cv2.waitKey()
cv2.destroyAllWindows()

print('Height of Image:', int(input1.shape[0]), 'pixels')
print('Width of Image:', int(input1.shape[1]), 'pixels')

cv2.imwrite('output.jpg', input1)
cv2.imwrite('output.png', input1)

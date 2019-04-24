#!/usr/bin/env python
# coding: utf-8

# ## Dilation, Erosion, Opening and Closing 

# In[3]:


import cv2
import numpy as np

image = cv2.imread('images/opencv_inv.png', 0)

cv2.imshow('Original', image)
cv2.waitKey(0)

# Let's define our kernel size
kernel = np.ones((5,5), np.uint8)

# Now we erode
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)

# 
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)

# Opening - Good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)

# Closing - Good for removing noise
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)


cv2.destroyAllWindows()


# ### There are some other less popular morphology operations, see the official OpenCV site:
# 
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

# In[ ]:





# In[ ]:





# In[ ]:





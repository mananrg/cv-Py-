#!/usr/bin/env python
# coding: utf-8

# ## Arithmetic Operations
# 
# These are simple operations that allow us to directly add or subract to the color intensity.
# 
# Calculates the per-element operation of two arrays. The overall effect is increasing or decreasing brightness.

# In[7]:


import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Create a matrix of ones, then multiply it by a scaler of 100 
# This gives a matrix with same dimesions of our image with all values being 100
M = np.ones(image.shape, dtype = "uint8") * 175 

# We use this to add this matrix M, to our image
# Notice the increase in brightness
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Likewise we can also subtract
# Notice the decrease in brightness
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


M = np.ones(image.shape, dtype = "uint8") * 75 
M


# In[ ]:





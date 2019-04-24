#!/usr/bin/env python
# coding: utf-8

# ## Let's take a closer look at color spaces
# 
# You may have remembered we talked about images being stored in RGB (Red Green Blue) color Spaces. Let's take a look at that in OpenCV.
# 
# ### First thing to remember about OpenCV's RGB is that it's BGR (I know, this is annoying)
# 
# Let's look at the image shape again. The '3L' 

# In[1]:


import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')


# ### Let's look at the individual color levels for the first pixel (0,0)

# In[5]:


# BGR Values for the first 0,0 pixel
B, G, R = image[10, 50] 
print B, G, R
print image.shape


# Let's see what happens when we convert it to grayscale

# In[7]:


gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print gray_img.shape
print gray_img[10, 50] 


# It's now only 2 dimensions. Each pixel coordinate has only one value (previously 3) with a range of 0 to 255

# In[8]:


gray_img[0, 0] 


# ### Another useful color space is HSV 
# Infact HSV is very useful in color filtering.

# In[11]:


#H: 0 - 180, S: 0 - 255, V: 0 - 255

image = cv2.imread('./images/input.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()


# ### Let's now explore lookng at individual channels in an RGB image

# In[12]:


image = cv2.imread('./images/input.jpg')

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

print B.shape
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's re-make the original image, 
merged = cv2.merge([B, G, R]) 
cv2.imshow("Merged", merged) 

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged) 

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


import cv2
import numpy as np

B, G, R = cv2.split(image)

# Let's create a matrix of zeros 
# with dimensions of the image h x w  
zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[19]:


image.shape[:2]


# #### You can view a list of color converisons here, but keep in mind you won't ever use or need many of these
# 
# http://docs.opencv.org/trunk/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0

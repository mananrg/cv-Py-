#!/usr/bin/env python
# coding: utf-8

# ## Translations
# 
# This an affine transform that simply shifts the position of an image.
# 
# We use cv2.warpAffine to implement these transformations.
# 

# In[1]:


import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Store height and width of the image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#       | 1 0 Tx |
#  T  = | 0 1 Ty |

# T is our translation matrix
T = np.float32([[1, 0, quarter_width], [0, 1,quarter_height]])

# We use warpAffine to transform the image using the matrix, T
img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', img_translation)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[3]:


# Let's take a look at T

print T


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





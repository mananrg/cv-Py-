#!/usr/bin/env python
# coding: utf-8

# ## Hi and welcome to your first code along lesson!
# 
# #### Reading, writing and displaying images with OpenCV

# Let's start by importing the OpenCV libary 

# In[1]:


# Press CTRL + ENTER to run this line
# You should see an * between the [ ] on the left
# OpenCV takes a couple seconds to import the first time

import cv2


# In[ ]:





# In[2]:


# Now let's import numpy
# We use as np, so that everything we call on numpy, we can type np instead
# It's short and looks neater

import numpy as np 


# Let's now load our first image

# In[3]:


# We don't need to do this again, but it's a good habit
import cv2 

# Load an image using 'imread' specifying the path to image
input = cv2.imread('./images/input.jpg')

# Our file 'input.jpg' is now loaded and stored in python 
# as a varaible we named 'image'

# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image varialbe
cv2.imshow('Hello World', input)

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before 
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey()

# This closes all open windows 
# Failure to place this will cause your program to hang
cv2.destroyAllWindows()


# In[ ]:


# Same as above without the extraneous comments

import cv2 

input = cv2.imread('./images/input.jpg')

cv2.imshow('Hello World', input)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Let's take a closer look at how images are stored

# In[16]:


# Import numpy
import numpy as np


# In[15]:


print input.shape


# #### Shape gives the dimensions of the image array
# 
# The 2D dimensions are 830 pixels in high bv 1245 pixels wide.
# The '3L' means that there are 3 other components (RGB) that make up this image.

# In[17]:


# Let's print each dimension of the image

print 'Height of Image:', int(input.shape[0]), 'pixels'
print 'Width of Image: ', int(input.shape[1]), 'pixels'


# ### How do we save images we edit in OpenCV?

# In[18]:


# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





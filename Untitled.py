#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Import the NUMPY package under the name npººº
import numpy as np


# In[6]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


# In[ ]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?


# In[9]:


a=np.random.random((2,3,5))


# In[10]:


a


# In[11]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))


# In[12]:


b


# In[ ]:


get_ipython().set_next_input('Do a and b have the same size? How do you prove that in Python code');get_ipython().run_line_magic('pinfo', 'code')


# In[14]:


np.shape(a) == np.shape(b)


# In[ ]:


#8. Are you able to add a and b? Why or why not?


# In[15]:


a + b


# Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# In[26]:


c = np.resize(b,(2,3,5))


# In[27]:


c


# In[28]:


d = a+c
d


# In[31]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Expl
print(a)

print(d)


# In[ ]:


la dif esta en que en d los valores tiene un +1


# In[ ]:


#12. Multiply a and c. Assign the result to e.


# In[34]:


e =a*c
e


# In[ ]:


#13. Does e equal to a? Why or why not?


# In[35]:


e == a
e y a son equivalentes porque e es el inverso de a


# In[ ]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


# In[36]:


d.max()


# In[37]:


d.min()


# In[38]:


d.mean()


# #15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

# In[46]:


f = np.empty(d.shape)
f


# In[ ]:


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


# In[48]:


d_min, d_max, d_mean = d.min(), d.max(), d.mean()
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100
f


# In[ ]:





# In[ ]:





# In[ ]:





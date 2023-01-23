#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1. Import the NUMPY package under the name npººº
import numpy as np


# In[11]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


# In[12]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?


# In[13]:


a=np.random.random((2,3,5))


# In[14]:


a


# In[15]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))


# In[16]:


b


# In[17]:


get_ipython().set_next_input('Do a and b have the same size? How do you prove that in Python code');get_ipython().run_line_magic('pinfo', 'code')


# In[ ]:


Do a and b have the same size? How do you prove that in Python code


# In[18]:


Do a and b have the same size? How do you prove that in Python code


# In[19]:


Do a and b have the same size? How do you prove that in Python code


# In[20]:


np.shape(a) == np.shape(b)


# In[21]:


#8. Are you able to add a and b? Why or why not?


# In[22]:


a + b


# Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# In[23]:


c = np.resize(b,(2,3,5))


# In[24]:


c


# In[25]:


d = a+c
d


# In[26]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Expl
print(a)

print(d)


# In[27]:


la dif esta en que en d los valores tiene un +1


# In[28]:


#12. Multiply a and c. Assign the result to e.


# In[29]:


e =a*c
e


# In[30]:


#13. Does e equal to a? Why or why not?


# In[31]:


e == a
e y a son equivalentes porque e es el inverso de a


# In[32]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


# In[33]:


d.max()


# In[34]:


d.min()


# In[35]:


d.mean()


# #15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

# In[36]:


f = np.empty(d.shape)
f


# In[37]:


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


# In[38]:


d_min, d_max, d_mean = d.min(), d.max(), d.mean()
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100
f


# In[39]:


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""


# In[43]:


g=np.empty(d.shape, dtype= object  )
d_min, d_max, d_mean = np.min(d), np.max(d), np.mean(d)
g[(d > d_min) & (d < d_mean)] = 'A'
g[(d > d_mean) & (d < d_max)] = 'B'
g[d == d_mean] = 'C'
g[d == d_min] = 'D'
g[d == d_max] = 'F'
g


# In[42]:


f


# In[ ]:





# In[ ]:





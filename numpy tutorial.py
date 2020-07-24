#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[37]:


a = np.array([1,23,4,5,6,7,8,9,9,8,9,6] ,dtype ='float')


# In[7]:


print(a)


# In[5]:


print(a)


# In[24]:


b = np.array([[[1],23,3], [1,2,3] , [2,a,2]])
print(b)


# In[25]:


b.ndim


# In[28]:


b[2][1].shape


# In[31]:


a.dtype


# In[34]:


b[2].itemsize


# In[36]:


b.nbytes


# In[3]:


f = np.array([[[1,2,3] , [1,2,3], [4,5,6]],[[2,3,4] ,[3,4,5] , [3,4,5]] , [[5,6,7],[4,5,6],[6,7,8]]])
print(f)


# In[4]:


f.dtype


# In[6]:


f.shape


# In[10]:


f.ndim


# In[16]:


print(f[ 1, 1 ,:])


# In[24]:


q = np.zeros((3, 3, 3))
print(q)


# In[25]:


#all 1s matrix
w = np.ones((3,3,3))


# In[26]:


print(w)


# # any other value

# In[27]:



a = np.full((3,3,3) , 90)
print(a)


# # full like method

# In[31]:



e=np.full_like( f ,50)
print(e)


# # random number start array 

# In[38]:



r = np.random.rand(3,3)*10
print(r)


# # random interger value 

# In[44]:



t = np.random.randint(0 , 2, size =(4,4))
print(t)


# # identity matix

# In[45]:



y = np.identity(4)
print(y)


# # reapit array 

# In[74]:



arr = np.array([1,2,3])
r1 = np.repeat(arr , 3 , axis = 0)
print("r1 = ")
print(r1)

arr1 = np.array([[1,2,3]])
r2 = np.repeat(arr1 , 3 , axis = 0)
print("r2 = ")
print(r2)


#if i change axis then


# # heree the axix is basically tell about from which dimention we want to repeat array like 0  means 3-d , 1 mean first inner box ,2 eans inside last bracket

# In[73]:


arr2 = np.array([[[1,2,3] , [4,5,6]] , [[2,3,4],[5,6,7]] , [[3,4,5],[6,7,8]]])
r3= np.repeat(arr2 , 2 , axis = 2)
print("r3 =" , r3)


# # coping one array to another with specified location

# In[72]:




final = np.ones((5,5))
print(final)
chg = np.zeros((3,3))
chg[1][1] = 9
print(chg)

final[1 : 4 , 1 :4] = chg
print(final)


# In[ ]:





# # be careful in copying 
# 
# 

# In[61]:


a = np.array([1,23,3])
b = a 
b[0] = 100
print(a)


# # mathematics

# In[63]:


a = np.array([1,2,3])
print(a)


# In[64]:


a +2


# In[65]:


a - 2


# In[66]:


a / 2


# In[67]:


a * 2


# In[68]:


a ** 3 #quab of array


# In[69]:


b  =np.array([3,4,5])
a + b


# In[70]:


np.sin(a)


# In[71]:


np.cos(a)


# # linear algebra

# In[79]:


a = np.full((2,3)  , 2)
print(a)

b = np.full((3,2) , 3)
print(b)


# # matrix multiplication

# In[80]:


c = np.matmul(a ,b)
print(c)


# In[85]:


c[1][1] = 19.0
#find the determinent of matrix
np.linalg.det(c)


# In[86]:


## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...


# # statistic

# In[100]:


stat = np.array([[7,2,1] ,
               [4,5,3]])
print(stat)


# In[101]:


np.min(stat ,axis = 0)
### without axis it will give overall max and min
### in this the compare wit 7-> 4 , 2-->5 , 1-->3


# In[104]:


np.max(stat ,axis = 1 )
## it will compare (7,2,1) and (4,5,3) and give max from each bracket


# # reorganising aray

# In[118]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before) 

after = before.reshape((2,2,2))
print(after)


# # vertical stack array

# In[119]:


v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])


# In[122]:


np.vstack([v1,v2]) 


# # horizontal stack 

# In[121]:


np.hstack([v1,v2])


# # Load data from file

# In[139]:


filedata = np.genfromtxt('data.txt'  ,delimiter = ',')
filedat =filedata.astype('int')
print(filedata)


# ## boolean masking and advance indexing

# In[141]:


filedata > 3 


# In[144]:


filedata[filedata> 4]
##data where it is grater then 4


# In[149]:


a = np.array([123,1242,42545,344,345,6785,7653,5634])
a[[1,3,4,5]]


# In[151]:


data = np.array([[1,13,21,11,196,75,4,3,34,6,7,8,0,1,2,3,4,5] , [3,42,12,33,766,75,4,55,6,4,3,4,5,6,7,0,11,12] , [1,22,33,11,999,11,2,1,78,0,1,2,9,8,7,1,76,88]])
print(data)


# In[154]:


np.any(data > 50 , axis = 0)
#this will give you that and of column data is > 50


# In[155]:


np.max(data)


# In[157]:


np.all(data > 195 , axis =0)
#this will give you the column in which all the element are > 195 


# In[ ]:





# In[ ]:





# In[ ]:





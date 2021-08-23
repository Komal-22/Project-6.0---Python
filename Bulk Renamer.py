#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def renamer():
    i = 0
    path = "/Users/apple/img2/"
    for filename in os.listdir(path):
        names = f"pic {i}.png"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()


# In[ ]:





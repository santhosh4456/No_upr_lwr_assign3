#!/usr/bin/env python
# coding: utf-8

# In[3]:


def str_check(s):
    d = {"UPPER_CASE":0, "lower_case":0}
    for x in s:
        if x.isupper():
            d["UPPER_CASE"]+=1
        elif x.islower():
            d["lower_case"]+=1
        else:
            pass
    print("Original string:", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["lower_case"])
str_check('The quick Brown Fox')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





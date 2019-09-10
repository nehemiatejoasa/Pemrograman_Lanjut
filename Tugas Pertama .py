#!/usr/bin/env python
# coding: utf-8

# In[25]:


dict_alay = {
    'i' : '1',
    'I' : '1',
    's' : '2',
    'R' : '2',
    'e' : '3',
    'E' : '3',
    'a' : '@',
    'A' : '4',    
    's' : '5',
    'S' : '5',
    'G' : '6',
    't' : '7',
    'T' : '7',
    'b' : '8',
    'B' : '8',
    'g' : '9',
    'o' : '0',
    'O' : '0',
    'k' : 'q',
    'K' : 'Q',
    'u' : 'v',
    'U' : 'V',
    '?' : '......????',
    '!' : '!!!????',
    
    
}


# In[26]:


def alay_huruf(h):
    if h in dict_alay:
        return dict_alay[h]
    else :
        return h


# In[27]:


def ganti_alay(n):
    kata_baru = ''
    for h in n :
        kata_baru += alay_huruf(h)
    return kata_baru


# In[28]:


masukan = input()
print(ganti_alay(masukan))


# In[ ]:





# In[ ]:





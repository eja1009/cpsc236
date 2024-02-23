#!/usr/bin/env python
# coding: utf-8

# In[5]:


def calculateSTR(items):
    subtotal = sum(items)
    sales_tax = subtotal * 0.06
    total_price = subtotal + sales_tax
    return total_price, sales_tax


# In[ ]:





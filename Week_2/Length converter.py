#!/usr/bin/env python
# coding: utf-8

# In[24]:


print("This is the weight converter :")


# In[25]:


source_unit = input("Please select initials for CURRENT unit of weight from following :\nM - Milligram \nG - Gram \nK - Kilogram \nT - Ton\n")


# In[26]:


weight = float(input('\nEnter weight:'))


# In[27]:


required_unit = input("\nPlease select initials for REQUIRED unit of weight from following :\nM - Milligram \nG - Gram \nK - Kilogram \nT - Ton\n")


# In[39]:


units = {'M': 0.001,'G': 1,'K': 1000,'T': 1000000,'m': 0.001,'g': 1,'k': 1000,'t': 1000000}

#CHECK IF THE ENTERED INPUT IS VALID OR NOT

try:

    #USE STD UNIT AS GRAM FOR EASY CAL    
    
    IN_gram = weight * units[source_unit]

    ans_weight = IN_gram / units[required_unit]

    #PRINT THE CONVERSION IN FLOAT
    print("After convertion\n")
    print(f"{weight} {source_unit} is equal to {ans_weight} {required_unit}")

except KeyError: 
    print("Invalid unit. Please choose from\n(m) milligram\n(g) gram\n(k) kilogram\n(t) ton")
except ZeroDivisionError:
    print("Conversion can't be in the same unit.")
except Exception as e:
    print("An error occured",{e})


# In[ ]:





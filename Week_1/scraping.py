#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
# URl of the website that we are scraping data from
page = requests.get("https://motioncut.shop/collections/colour-grading-luts")

# using html parser to get html file data in readable formate
soup = BeautifulSoup(page.content,"html.parser")

title = soup.findAll(attrs ={"class" : "grid-product__title grid-product__title--body"})
  
price = soup.findAll(attrs ={"class" : "grid-product__price--original"})
    
dis = soup.findAll(attrs ={"class" : "grid-product__price--savings"})
    
    
price_list = []    
name_list = []
dis_list = []      

# created a DataFrame to store data 
df = pd.DataFrame()
    
for x in range(0,14):
    
    names = title[x].text.replace('/n',"")
    name_list.append(names)
    
    prices = price[x].text.replace('/n',"")
    price_list.append(prices)
                           
    discount = dis[x].text.replace('\n',"").replace(" ","")
    dis_list.append(discount)

    
df['Product'] = name_list
df['Price'] = price_list  
df['Discount']  = dis_list

df.to_csv("MotionCut_items.csv")

df



# In[37]:


import random

random_int = random.randint(1, 100)

print("Guess the num between 1 to 100")
print("You get 5 guesses")
for x in range(5,0):
    print(x,"st guess")
    guess = int(input("Enter your guess"))
    if(guess>=1 and guess<=100):
        if(guess == random_int):
            print("Congrates!! you guessed it right")
        elif(guess > random_int):
            print("you guessed a little high \n Try again")
        else:
            print("you guessed a little low \n Try again")
    else:
        print("Please enter a num between 1 to 100")
    print("No. of guesses left",x)


# In[ ]:





# In[ ]:





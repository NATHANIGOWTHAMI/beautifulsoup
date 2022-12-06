#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

search_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Mount+Pleasant%2C+MI"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

my_data = []
data={}

response = requests.get(search_url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')

for item in soup.select('[class*=container]'):
    
    try:
        if item.find("h3"):
            h3_data= item.find("h3").get_text()
            print(h3_data)
            reviews=item.select('[class*=css-chan6m]')[0].get_text()
            print(reviews)
            rating=item.select('[aria-label*=rating]')[0]['aria-label']
            print(rating)
            pricerange= item.select('[class*=priceRange]')[0].get_text()
            print(pricerange)
            description=item.select('[class*=css-16lklrv]')[0].get_text()
            print(description)
            
            print("_______")
            
            my_data.append({"Name": h3_data, "reviews": reviews, "rating": rating, "pricerange": pricerange ,"description": description})
    except Exception as e:
        #raise e
        print("")
print(my_data)
data={"Name": h3_data, "reviews": reviews, "rating": rating, "pricerange": pricerange ,"description": description}

df = pd.DataFrame(my_data)
header=['Name','reviews','rating','pricerange','description']

df1=df.to_csv('restaurents_mount_pleasant.csv',columns=header)


# In[ ]:





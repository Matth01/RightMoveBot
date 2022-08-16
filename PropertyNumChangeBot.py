#!/usr/bin/env python
# coding: utf-8

# In[7]:


from rightmove_webscraper import RightmoveData
import pandas as pd
url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=USERDEFINEDAREA%5E%7B%22id%22%3A7805129%7D&sortType=6&savedSearchId=42905534&maxBedrooms=3&minBedrooms=2&maxPrice=1500&radius=0.0&propertyTypes=&mustHave=&dontShow=&includeLetAgreed=false&furnishTypes='
rm = RightmoveData(url)
current_val = rm.results_count
print(rm.results_count)

f = open("num.txt", "r")
prev_val=int(f.read())

import requests
if (prev_val != current_val):
    print("SEND MESSAGE")
    requests.get("https://api.telegram.org/bot5500222247:AAH2Ajp7wzvCusaiwwpX_dczxwnMfX45FKE/sendMessage?chat_id=-1001721932075&text=New Property")
else:
    print("NO CHANGE")
    
f = open("num.txt", "w")
f.write(str(current_val))
f.close()


# In[ ]:





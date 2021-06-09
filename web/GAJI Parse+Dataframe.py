#!/usr/bin/env python
# coding: utf-8

# In[215]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')


# In[216]:


import re
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_lg")


# In[217]:


from bs4 import BeautifulSoup
with open("GAJI.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# In[218]:


content = soup.find_all("div", class_ = 'ocr_carea')
len(content)


# In[219]:


results = []

for result in content: 
    result = result.text
    result = result.replace("\n", " ")
    results.append(result)


results = results[114:2959]
results = (''.join(results))


# In[220]:


sec_results = re.split(('\d{2}\.\d{3}'), results)


# In[221]:


list = re.findall(('\d{2}\.\d{3}'), results)
print(list)


# In[222]:


results_clean = []
for string in sec_results:
    if (string != ""):
        results_clean.append(string)
print(results_clean)


# In[223]:


type(results_clean)


# In[224]:


len(list)


# In[225]:


doc = results_clean[1:816]


# In[226]:


len(doc)


# In[227]:


docdf = pd.DataFrame([],columns=["section","text","vector"])


# In[228]:


for x in doc:
    #print(x)
    docdf["section"] = list
    docdf = docdf.append(pd.DataFrame([[x, None]], columns=["text","vector"]), ignore_index=True)


# In[ ]:


def vectorize(row):
    return nlp(row["text"]).vector


# In[ ]:


docdf


# In[ ]:


docdf["vector"] = docdf.apply(vectorize, axis=1)


# In[ ]:


docdf


# In[ ]:


docdf.to_csv("GAJI.csv", index=False, encoding='utf-8')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[187]:


d=pd.read_csv("C:\\Users\\91966\\Desktop\\Nandini python\\mens_t20.csv")


# In[188]:


d


# In[189]:


d.head()


# In[190]:


d.tail()


# In[191]:


d.shape


# In[192]:


d.info()


# In[193]:


d.describe()


# In[194]:


d.isna()


# In[195]:


d.isnull()


# In[196]:


d.isnull().sum()


# In[197]:


d.isnull().any()


# In[198]:


d["Team"]


# In[199]:


d["Team"].head(20)


# In[226]:


a=d["Team"].unique()
print(a)
len(a)


# In[201]:


d["Team"] == "India"


# In[202]:


team = d["Team"]
count = 0  # Initialize counter

for i in team:
    if i == "India":
        print(i)
        count += 1  # Increment the counter each time "India" is found

print(count)  # Print the total count of "India"


# In[203]:


d["Team"].value_counts()


# In[204]:


d["NO"].value_counts()


# In[205]:


sns.barplot(data=d,x="Player",y="NO")


# In[206]:


d["Runs"].sort_values()


# In[207]:


d["Runs"].sort_values().tail()


# In[208]:


d


# In[209]:


top_5 = d.nlargest(5, 'Runs')[["Player","Runs"]]

print(top_5)



# In[210]:


top_5=d.nlargest(5,"Runs")
print(top_5)


# In[211]:


d.sort_values("Runs")


# In[212]:


d.sort_values("Runs").tail()


# In[213]:


a=d["Player"].unique()


# In[214]:


len(a)


# In[215]:


d


# In[216]:


d["Runs"]>100


# In[230]:


filtered_data = d[d['Runs'] > 200]
filtered_data.set_index('Player')['Runs'].plot.pie(autopct='%1.1f%%',  figsize=(7, 7), title="Runs Distribution by Player (Runs > 100)")
plt.show()


# In[231]:


sns.barplot(d,y="Team",x="Runs")
plt.show()


# In[219]:


d


# In[220]:


team_runs = d.groupby('Team')['Runs'].sum()

# Plot pie chart for runs by team
team_runs.plot.pie(autopct='%1.1f%%', figsize=(7, 7), title="Runs Distribution by Team")

# Display the plot
plt.show()


# In[221]:


sns.barplot(d,y="Player",x="100")
plt.show()


# In[222]:


sns.barplot(d,y="Team",x="0")
plt.show()


# In[223]:


d


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df=pd.read_csv(r'C:\Users\HP\Desktop\Diwali sales dataset\Diwali Sales Data.csv', encoding='unicode_escape')


# In[7]:


df.shape


# In[8]:


df.head(10)


# In[9]:


df.info()


# # drop unrelated/blank columns

# In[21]:


df.drop('Status', axis=1, inplace=True)



# In[24]:


pd.isnull(df)


# In[26]:


pd.isnull(df).sum() #check all null value


# In[28]:


df.shape


# In[29]:


df.dropna(inplace=True)#drop null values


# In[30]:


pd.isnull(df).sum()


# In[33]:


#intialization list of lists
data_test = [['mahadev',11],['Gopi',15],['keshav',],['lalita',16]]

# create the pandas dataframe using list
df_test = pd.DataFrame(data_test, columns=['Name','Age'])

df_test


# In[35]:


df_test.dropna(inplace=True)


# In[36]:


df_test


# In[37]:


#change datatype
df['Amount'] = df['Amount'].astype('int')


# In[38]:


df['Amount'].dtypes


# In[39]:


df.columns


# In[41]:


#describe() method returns description of the data in the dataframe(i.e,count,mean,std,etc)
df.describe()


# In[65]:


#rename column
df.info()


# In[43]:


#use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 

# # Gender

# In[44]:


sns.countplot(x='Gender',data = df)


# In[45]:


#it give us total value on the bar 
ax=sns.countplot(x='Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[47]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Gender',y='Amount',data=sales_gen)


# # from above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# Age

# In[49]:


ax=sns.countplot(data=df,x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


#Total Amount vs Age Group 
sales_Age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount' ,data = sales_Age)


# from above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# state

# In[62]:


#total number of orders from top 10 states
sales_State = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data=sales_State, x='State',y='Orders')


# In[61]:


#total amount/sales from top 10 states
sales_State = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_State, x='State',y='Amount')


# From above graphs we can see that unexpectedly most of the orders are from uttar pradesh, Maharashrta and karanataka respectively but total sale/amount is from UP , karnataka and then Maharashtra

# occupation

# In[68]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data = df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[69]:


sales_State = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_State, x='Occupation',y='Amount')


# *from above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector* 

# *product category*

# In[71]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data = df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[72]:


sales_State = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_State, x='Product_Category',y='Amount')


# *From above graphs we can see that most of the sold products are from Food,clothing,Footwear and Electronics Category*

# In[78]:


# top 10 most sold products (same things as above)

fig1,ax1=plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# *conclusion:*

# *Married woman age group 26-35yrs from UP,Maharastra and Karnataka working in IT,Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics Category*

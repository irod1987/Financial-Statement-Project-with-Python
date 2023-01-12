#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# In[10]:


#Solution
#Calculate Profit As The Differences Between Revenue And Expenses
profit = []

for i in range (0, len(expenses)):
    profit.append(revenue[i] - expenses [i])
print (profit)
print (len(profit))


print(sum(profit))


# In[12]:


#Calculate Tax As 30% Of Profit And Round To 2 Decimal Points
tax = [round(i * 0.3, 2) for i in profit]
print (tax)
print (len(tax))


# In[18]:


#Calculate Profit Remaining After Tax Is Deducted
profit_after_tax = []
for i in range (0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])
print (profit_after_tax)
print (len(profit_after_tax))
print ( sum (profit_after_tax))


# In[16]:


#Calculate The Profit Margin As Profit After Tax Over Revenue
#Round To 2 Decimal Points, Then Multiply By 100 To Get %
profit_margin = []
for i in range (0, len(profit_after_tax)):
    profit_margin.append(profit_after_tax[i] / revenue[i])
profit_margin

profit_margin = [round((i * 100),2) for i in profit_margin]

profit_margin


# In[19]:


#Calculate The Mean Profit After Tax For The 12 Months
mean_pat = sum(profit_after_tax) / len(profit_after_tax)
mean_pat


# In[21]:


#Find The Months With Above-Mean Profit After Tax
good_months = []
for i in range (0, len(profit_after_tax)):
    good_months.append(profit_after_tax [i] > mean_pat)
good_months


# In[22]:


#Bad Months Are The Opposite Of Good Months!
bad_months = []
for i in range (0, len(profit_after_tax)):
    bad_months.append(not (good_months[i]))
bad_months


# In[23]:


#The Best Month Is Where Profit After Tax Was Equal To The Maximum
best_month = []
for i in range (0, len(profit_after_tax)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
best_month


# In[24]:


#The Worst Month Is Where Profit After Tax Was Equal To The Minimum
worst_month = []
for i in range (0, len(profit_after_tax)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
worst_month


# In[27]:


#Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i/1000,2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 0) for i in profit_after_tax]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]


# In[28]:


#Print Results
print ("Revenue :") 
print (revenue_1000)
print ("Expenses :") 
print (expenses_1000)
print ("Profit :")
print(profit_1000)
print ("Profit after tax :")
print (profit_after_tax_1000)
print ("Profit margin :")
print (profit_margin)
print ("Good months :")
print (good_months)
print ("Bad months :")
print (bad_months)
print ("Best month :")
print (best_month)
print ("Worst month :")
print (worst_month)


# In[ ]:





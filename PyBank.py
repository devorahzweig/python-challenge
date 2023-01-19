#!/usr/bin/env python
# coding: utf-8

# In[33]:


import csv
import os
file = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    #reading the file
    csvreader = csv.reader(csvfile, delimiter = ',')
    #making sure the program sees that there is a header
    header = next(csvreader)
    #defining our variables and dicts
    profits = []
    change_profit = []
    monthly_count = []
    for row in csvreader:
        #creating a count for the amount of months and profits
        monthly_count.append(row[0])
        profits.append(int(row[1]))
    for i in range(len(profits)-1):
        change_profit.append(profits[i+1]-profits[i])
#finding the maximum and minimum change in profits
increase = max(change_profit)
decrease = min(change_profit)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1
#printing results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(monthly_count)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {monthly_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {monthly_count[month_decrease]} (${(str(decrease))})")

with open('PyBank_results.txt', "w") as txt_file:
    txt_file.write("Financial Analysis:\n")
    txt_file.write("------------------\n")
    txt_file.write("Total Months:"+ str({len(monthly_count)}) + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Total: $"+str({sum(profits)})+"\n")
    txt_file.write("-------------------\n")
    txt_file.write("Average Change:"+ str({round(sum(change_profit)/len(change_profit),2)})+"\n")
    txt_file.write("-------------------\n")
    txt_file.write("Greatest Increase in Profits:"+ str({monthly_count[month_increase]})+"$"+str(increase)+"\n")
    txt_file.write("-------------------\n")
    txt_file.write("Greatest Decrease in Profits:"+ str({monthly_count[month_decrease]})+"$"+str(decrease)+"\n")
    


# In[ ]:





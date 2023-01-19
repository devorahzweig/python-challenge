#!/usr/bin/env python
# coding: utf-8

# In[56]:


import csv
import os
#defining our variables and lists
candidates=[]
all_candidates=[]
percent=[]
voting_df={}
total=0
with open('election_data.csv', 'r') as file:
    #reading the file
    reader = csv.reader(file)
    for row in reader:
        total+=1 #increasing the total based on the number of rows
        all_candidates.append(row[2])
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total-=1
for i in range(1,len(candidates)): #loop to count the number of votes
    count=0
    for j in range(len(all_candidates)):
        if candidates[i]==all_candidates[j]:
            count+=1
    voting_df[candidates[i]]=count
candidates.remove(candidates[0])
print("Election Results:")
print("-----------------")
print("Total Votes: %d"%total)
print("-------------------")
for i in candidates:
    #finding the percentage of votes per each candidate
    percentage=(voting_df[i]/total)*100
    percent.append(percentage)
    print("%s : %f(%d)"%(i,percentage,voting_df[i]))
print("------------------------------------------")
print("Winner:", candidates[percent.index(max(percent))])
print("----------------------")


with open('PyPoll_results.txt', "w") as txt_file:
    txt_file.write("Election Results:\n")
    txt_file.write("-----------------\n")
    txt_file.write("Total Votes: %d"%total+"\n")
    txt_file.write("-------------------\n")
    for i in candidates:
        percentage=(voting_df[i]/total)*100
        percent.append(percentage)
        txt_file.write("%s : %f(%d)"%(i,percentage,voting_df[i])+"\n")
    txt_file.write("------------------------------------------\n")
    txt_file.write("Winner:"+ candidates[percent.index(max(percent))]+"\n")
    txt_file.write("----------------------")
    


# In[ ]:





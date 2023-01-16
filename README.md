# python-challenge
PyPoll
import csv
import os
candidates=[]
all_candidates=[]
percent=[]
voting_df={}
total=0
with open('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        total+=1
        all_candidates.append(row[2])
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total-=1
for i in range(1,len(candidates)):
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
    percentage=(voting_df[i]/total)*100
    percent.append(percentage)
    print("%s : %f(%d)"%(i,percentage,voting_df[i]))
print("------------------------------------------")
print("Winner:", candidates[percent.index(max(percent))])
print("----------------------")

PyBank
import csv
import os
file = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    profits = []
    change_profit = []
    monthly_count = []
    for row in csvreader:
        monthly_count.append(row[0])
        profits.append(int(row[1]))
    for i in range(len(profits)-1):
        change_profit.append(profits[i+1]-profits[i])
increase = max(change_profit)
decrease = min(change_profit)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1
print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(monthly_count)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {monthly_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {monthly_count[month_decrease]} (${(str(decrease))})")      

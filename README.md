# python-challenge
PyPoll
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


PyBank
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

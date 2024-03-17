import os
import csv
import statistics
from statistics import mean

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #print(csvreader)

    Total_Profits = 0
    Total_Months = []
    Profit_loss = []
    


    for row in csvreader:

        Total_Months.append(row[0])
        Total_Profits = Total_Profits + int(row[1])
        Profit_loss.append(int(row[1]))
   
    
    #To calculate the Revenue i need to substract the current period revenue to the prior period revenue
    #Then ill put it in a list and find the mean 
            
    Change_Rev = []

    for x in range(1,len(Profit_loss)):
        Change_Rev.append((int(Profit_loss[x])) - int(Profit_loss[x-1]))


    #Using the main funtion from statistics
    average = statistics.mean(Change_Rev)
    #Using the pre existing funtion in python i can find Max and Min Value
    Max_inc = max(Change_Rev)
    Min_inc = min(Change_Rev)

    #Find the Date that matches the value 
    Date_Inc = Total_Months[Change_Rev.index(max(Change_Rev))+1]
    Date_Dec = Total_Months[Change_Rev.index(min(Change_Rev))+1]

    #Print the value and compare it matches the one in the answer sheet
    #print(Date_Dec)
    #print(Date_Inc)


    #Print all the results 

    print("Finanacial Analysis ")
    print("---------------------------------------")
    print("Total Months: " + str(len(Total_Months)))    #Amount of months in the list
    print("Total: " + "$" + str(Total_Profits)) #Total profits 
    print("Average Change: " + "$" + str(round(average, 2))) #Averge change 
    print("Greatest Inrease in Profits: " + Date_Inc , "$"+ str(Max_inc)) #Max Value
    print("Greatest Decrease in Profits: " + Date_Dec, "$"+ str(Min_inc)) #Min Value

    # Read the header row first (skip this step if there is no header
    #print(f"CSV Header: {csv_header}")

   
import os
import csv
import statistics
from statistics import mean

csvpath = os.path.join('/Users/andreacastrogutierrez/Desktop/PythonChallenge/Pybank/Resources/budget_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #print(csvreader)
    
    #Stablish Starter Values 
    Total_Profits = 0
    Total_Months = []
    Profit_loss = []
    
    
    #loop thru the file to create the lists needed 
    for row in csvreader:

        Total_Months.append(row[0])
        Total_Profits = Total_Profits + int(row[1])
        Profit_loss.append(int(row[1]))
   
    
#To calculate the Revenue i need to substract the current period revenue to the prior period revenue
#Then ill put it in a list and find the mean
            
    Change_Rev = []

    for x in range(1, len(Profit_loss)):
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
    print("Total: " +  '${:,.0f}'.format(Total_Profits)) #Total profits 
    print("Average Change: " + '(${:,.2f})'.format(round(average,2))) #Averge change 
    print("Greatest Increase in Profits: " + Date_Inc , '(${:,.0f})'.format(Max_inc)) #Max Value
    print("Greatest Decrease in Profits: " + Date_Dec, '(${:,.0f})'.format(Min_inc)) #Min Value

    # Read the header row first (skip this step if there is no header
    #print(f"CSV Header: {csv_header}")


    with open('Pybank.txt', 'w') as f:
     f.write("Finanacial Analysis ")
     f.write("\n")
     f.write("---------------------------------------")
     f.write("\n")
     f.write("Total Months: " + str(len(Total_Months))) #Amount of months in the list
     f.write("\n")   
     f.write("Total: " +  '${:,.0f}'.format(Total_Profits)) #Total profits
     f.write("\n")  
     f.write("Average Change: " + '(${:,.2f})'.format(round(average,2))) #Averge change 
     f.write("\n") 
     f.write("Greatest Increase in Profits: " + str(Date_Inc)  + '(${:,.0f})'.format(Max_inc)) #Max Value
     f.write("\n")
     f.write("Greatest Decrease in Profits: " + str(Date_Dec)  + '(${:,.0f})'.format(Min_inc)) #Min Value
     f.close()


   
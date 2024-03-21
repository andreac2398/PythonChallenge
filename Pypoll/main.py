import os
import csv

csvpath = os.path.join("/Users/andreacastrogutierrez/Desktop/PythonChallenge/Pypoll/Resources/election_data.csv")

with open(csvpath,newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Stablish the values i need to start the analysis 
    Total_Votes = 0 
    Candidate = []
    Votes_plus_candidate = {}

    for row in csvreader:

        Total_Votes += 1
        Candidate_Name = row[2]
        

        if Candidate_Name not in Candidate:

            Candidate.append(Candidate_Name)
            Votes_plus_candidate[Candidate_Name] = 0
        Votes_plus_candidate[Candidate_Name] += 1


 #Find the % that represent the amount of votes of each candidate
    
    cand1 = Candidate[0]
    Total_Votes_Cand1 = int(Votes_plus_candidate.get(cand1)) #Finds the Value that goes with each key
    Percent_Cand1 = (Total_Votes_Cand1 * 100)/Total_Votes #Rule of 3

    cand2 = Candidate[1]
    Total_Votes_Cand2 = int(Votes_plus_candidate.get(cand2)) 
    Percent_Cand2 = (Total_Votes_Cand2 * 100)/Total_Votes 

    cand3 = Candidate[2]
    Total_Votes_Cand3 = int(Votes_plus_candidate.get(cand3)) 
    Percent_Cand3 = (Total_Votes_Cand3 * 100)/Total_Votes 

#Compare the vote results and decide who is the winner 
    winner = 0
    if (Total_Votes_Cand1 > Total_Votes_Cand2) and (Total_Votes_Cand1 > Total_Votes_Cand3):
        winner = Candidate[0]
    elif (Total_Votes_Cand2 > Total_Votes_Cand1) and (Total_Votes_Cand2 > Total_Votes_Cand3):
        winner = Candidate[1]
    else:
        winner = Candidate[3]           

#Printing the results 
    print("Election Results ")
    print("----------------------------") 
    print("Total Votes: " , Total_Votes)
    print("----------------------------")
    print( str(cand1) ,': ' , '{:.3f}%'.format(Percent_Cand1), '('+str(Votes_plus_candidate.get(cand1))+')' )
    print( str(cand2) ,': ' , '{:.3f}%'.format(Percent_Cand2), '('+str(Votes_plus_candidate.get(cand2))+')' )
    print( str(cand3) ,': ' , '{:.3f}%'.format(Percent_Cand3), '('+str(Votes_plus_candidate.get(cand3))+')' )
    print("-----------------------------")
    print("Winner:" , winner)

    
 
  

    with open('Pypoll.txt', 'w') as f:
     f.write("Election Results ")
     f.write("\n")
     f.write("---------------------------------------")
     f.write("\n")
     f.write("Total Votes: " + str(Total_Votes)) 
     f.write("\n")   
     f.write(str(cand1) + ': ' + '{:.3f}%'.format(Percent_Cand1) +  '('+str(Votes_plus_candidate.get(cand1))+')' ) 
     f.write("\n")  
     f.write(str(cand2) + ': ' + '{:.3f}%'.format(Percent_Cand2) +  '('+str(Votes_plus_candidate.get(cand2))+')')  
     f.write("\n") 
     f.write(str(cand3) + ': ' + '{:.3f}%'.format(Percent_Cand3) +  '('+str(Votes_plus_candidate.get(cand3))+')' ) 
     f.write("\n")
     f.write("-----------------------------") 
     f.write("\n")
     f.write("Winner:" + str(winner))
     f.close()
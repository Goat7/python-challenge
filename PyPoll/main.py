import os
import csv

#Set filepath and import csv file
input_file = input("Enter the name of the CSV file(s) you will like to process one at a time? ")
filepath = os.path.join(input_file)
with open(filepath, newline = '') as csvfile:
    csvdata = csv.reader(csvfile, delimiter = ',')
    header = next(csvdata)
    
    #Create lists
    voterid = []
    county = []
    candidates = []
    names_of_candidates = []


    #Run a for loop for every x of data
    for x in csvdata:
        voterid.append(x[0])
        county.append(x[1])
        candidates.append(x[2])
    
    #Create variables. 
    voters_list = len(voterid)
    candidates_list = set(candidates) #Set function is used to identify each unique candidate


    print("Election Results")
    print("-----------------------------------------------")
    print(f"The Total number of votes cast: {voters_list}")
    print("------------------------------------------------")



  
    for x in candidates_list:
        names_of_candidates.append(x)

    #Create a dictionary for the candidates
    dict_of_candidates = {}
    candidates_count = 0
    for x in names_of_candidates:
        candidate_name = str(names_of_candidates[candidates_count])
        votes = int(candidates.count(candidate_name))
        vote_share = round(votes/voters_list * 100, 2)
        dict_of_candidates.update({candidate_name: votes})
        print(f"{candidate_name}: {vote_share}%  ({votes})")
        candidates_count = candidates_count + 1

    

    winner = max(dict_of_candidates, key=lambda key: dict_of_candidates[key])
    
    print("--------------------")
    print("Winner: ", winner)
    print("--------------------")

  
txt_file = open("Election_Results.txt", "w")
txt_file.write("Election_Results\n")
txt_file.write("----------------------------------------------- 1 \n")
txt_file.write(f"The Total number of votes cast: {voters_list}\n")
txt_file.write("------------------------------------------------ 1 \n")
txt_file.write(f" {candidate_name}: {vote_share}  {votes}\n")
txt_file.write(f" {candidate_name}: {vote_share}  {votes}\n")
txt_file.write(f" {candidate_name}: {vote_share}  {votes}\n")
txt_file.write(f" {candidate_name}: {vote_share}  {votes}\n")
#txt_file.write(f" {candidate_name}\n")
#txt_file.write(f" ${vote_share}\n")
#txt_file.write(f" ${votes}\n")
txt_file.write("------------------------------------------------ 1 \n")
txt_file.write(f"Winner: {winner}\n")
txt_file.write("------------------------------------------------ 1 \n")
txt_file.close()
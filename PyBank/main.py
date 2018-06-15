#import os and write csv path
from statistics import mean
import os
input_file = input("Enter the name of the CSV file(s) you will like to process one at a time? ")
csvpath = os.path.join(input_file) 
#csvpath = os.path.join("budget_data_1.csv") 

#Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader delimiter and varaiable
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader,None)
    csvlist = list(csv_reader)

    #list creation, places to store csv "rows" (They are columns!)
    dates = []
    revenues = []

    #run for loop for every row
    for x in csvlist:
        dates.append(x[0])
        revenues.append(int(x[1]))
    
    #create a list for revenue change
    revchange = []

    #run loop through revenues list to find the change revenues from month
    revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    #variables
    max_change = max(revchange)
    big_loss = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    max_month = None
    loss_month = None

    
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == big_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])
    

    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"The financial analysis occured over {total_month} months")
    print(f"The average revenue change was ${avg_change}")
    print(f"The maximum revenue gain was ${max_change} and occured on {max_month}")
    print(f"The biggest revenue loss was ${big_loss} and occured on {loss_month}")

txt_file = open("Company_Financial_Analysis_Budget_1.txt", "w")
txt_file.write("Company Financial Analysis Budget 1 \n")
txt_file.write("-----------------------------------------------------------------------------\n")
txt_file.write(f"Total Months: {total_month}\n")
#txt_file.write(f"Total Revenue: ${rev_total}\n")
txt_file.write(f"Average Revenue Change: ${avg_change}\n")
txt_file.write(f"Maximum Revenue Gain: ${max_change} in {max_month}\n")
txt_file.write(f"Largest Revenue Loss: ${big_loss} in {loss_month}\n")
txt_file.close()
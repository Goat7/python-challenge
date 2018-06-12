import os
import csv


csvpath = os.path('C:\Users\chuck\GWDC201805DATA3-Class-Repository-DATA\python-challenge\PyBank\budget_data_1.csv')


with open(csvpath, newline ='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')

   print(csvreader)
  


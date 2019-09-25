
# https://www.geeksforgeeks.org/working-csv-files-python/

# importing the csv module 
import csv 

# field names 
fields = ['Id', 'Name'] 

# data rows of csv file 
rows = [['1', 'Sophia'], ['2', 'Sam']]

# name of csv file 
filename = "names.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    
    # writing the fields 
    csvwriter.writerow(fields) 

    # writing the data rows 
    csvwriter.writerows(rows)

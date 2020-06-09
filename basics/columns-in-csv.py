import csv

with open('csvfiles/all.csv', 'r') as csvfile:
     first_line = csvfile.readline()
     print(first_line)
     ncol = first_line.count(',') + 1
     print("Number of columns: %s" % ncol)
     

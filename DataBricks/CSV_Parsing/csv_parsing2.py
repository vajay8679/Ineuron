import csv

with open('employees1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
 
    with open('employees2.csv','w') as csv_write:
        write_file = csv.writer(csv_write,delimiter="-")
   
        for item in csv_reader:
            write_file.writerow(item)
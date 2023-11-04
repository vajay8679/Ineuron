import csv

row = ['David', 'MCE', '3', '7.8']

row1 = ['Lisa', 'PIE', '3', '9.1']

row2 = ['Raymond', 'ECE', '2', '8.5']

with open('emp.csv','a') as csv_file:

    csv_write = csv.writer(csv_file)

    csv_write.writerow(row)
    csv_write.writerow(row1)
    csv_write.writerow(row2)
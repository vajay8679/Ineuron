import csv

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [ ['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

with open('studnet.csv','w') as write_file:
    writer_file = csv.writer(write_file)
    writer_file.writerow(rows)
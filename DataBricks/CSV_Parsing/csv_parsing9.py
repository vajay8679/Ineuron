import csv

fields = ['Name', 'Email']
 
# data rows of csv file
rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
        ['Sanchit', 'sanchit.gfg@gmail.com'],
        ['Aditya', 'aditya.gfg@gmail.com'],
        ['Sagar', 'sagar.gfg@gmail.com'],
        ['Prateek', 'prateek.gfg@gmail.com'],
        ['Sahil', 'sahil.gfg@gmail.com']]

with open('email.csv','w') as email_csv:
    email_file = csv.writer(email_csv)

    email_file.writerow(fields)
    email_file.writerows(rows)
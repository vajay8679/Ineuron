import csv

#Writing a dictionary to a CSV file

mydict =[{'branch': 'COE', 'cgpa': '9.0', 
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1', 
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3', 
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5', 
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8', 
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1', 
         'name': 'Sahil', 'year': '2'}]
 
# field names
fields = ['name', 'branch', 'year', 'cgpa']


with open('student1.csv','w') as csv_file:
    writer_file = csv.DictWriter(csv_file, fieldnames=fields)

    writer_file.writeheader()

    writer_file.writerows(mydict)
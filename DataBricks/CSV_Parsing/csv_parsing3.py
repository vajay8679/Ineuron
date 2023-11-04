import csv

with open('employees1.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
 
    with open('employees3.csv','w') as csv_write:
        fieldnames = ['empId', 'empName', 'gender', 'salary', 'department']
        write_file = csv.DictWriter(csv_write,fieldnames=fieldnames,delimiter="\t")
   
        write_file.writeheader()
        for item in csv_reader:
            del item['salary']
            write_file.writerow(item)
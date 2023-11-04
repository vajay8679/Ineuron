import csv

with open('employees1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # csv_reader = csv.DictReader(csv_file)


    # print(csv_reader)

    # next(csv_reader) #to remove column row used only with -> csv.reader(csv_file) and not used with -> csv.DictReader(csv_file)
    for item in csv_reader:
        # print(item[0])  used that kind of thing with csv.reader()
        # print(item['empName'])   #used that kind of thing with csv.DictReader()

        # name = item['empName'] #used that kind of thing with csv.DictReader()
        # gender = item['gender'] #used that kind of thing with csv.DictReader()
        # salary = item['salary'] #used that kind of thing with csv.DictReader()

        # print(name,gender,salary) #used that kind of thing with csv.DictReader()



        name = item[1] #used that kind of thing with csv.reader()
        gender = item[2] #used that kind of thing with csv.reader()
        salary = item[3] #used that kind of thing with csv.reader()

        print(name,gender,salary) #used that kind of thing with csv.reader()

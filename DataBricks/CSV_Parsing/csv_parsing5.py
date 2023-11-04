import csv

with open('emp_birthday.txt','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    count_num = 0

    for item in csv_reader:
        if count_num == 0:
            print(f'Column are given as { ",".join(item)}')
            count_num += 1
        else:
            print(f'\t {item[0]} work in the {item[1]} department and was born in {item[2]}.')
            count_num += 1
    print(f'Processed {count_num} lines.')
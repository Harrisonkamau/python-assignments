import csv
with open('MOCK_DATA.csv', 'r') as csvfile:
    id_number = raw_input('Enter your id please: ')
    data_reader = csv.reader(csvfile, delimiter=',')

    for row in data_reader:
        if id_number == row[0]:
            print 'my first name is: '+row[1] + 'and you can email me at: '+row[3] + 'and, uh my ip address is: '+row[5]











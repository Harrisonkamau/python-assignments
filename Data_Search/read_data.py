
# Instructions
# Go to http://mockaroo.com/ and create csv data up to any number
# Create a Python file
# Read through the csv file and prompt the user to input an id
# If the id matches any id in the csv data, then print out the first name,email
# and ip address that correspond to that particular id


import csv  # import csv module
with open('MOCK_DATA.csv', 'r') as csvfile:   # read the csv file
    id_number = raw_input('Enter your id please: ')  # prompt the user for an id
    data_reader = csv.reader(csvfile, delimiter=',')  # read the file,slicing the commas

    for row in data_reader:  # iterate through the data and compare to the given id
        if id_number == row[0]:
            # print the first name, email and ip address
            print 'my first name is: '+row[1] + ' and you can email me at: '+row[3] + ' and, uh my ip address is: '+row[5]

        else:
            pass











import os
# create a function that saves data


def save_data(data, filename):
    data = raw_input("What diploma course are you currently pursuing?: ")
    with open('diploma.txt', 'w') as dt:
        dt.write(string_from_data(data))


def retrieve_data(filename):
    with open('diploma.txt') as dt:
        return data_from_string(dt.read())


def string_from_data(data):
    return ''.join(data)


def data_from_string(s):
    return s.split('\n')


FILENAME = 'diploma.txt'
if os.path.isfile(FILENAME):
    mylist = retrieve_data(FILENAME)
else:
    mylist = []

save_data(mylist, FILENAME)


print retrieve_data('diploma.txt')



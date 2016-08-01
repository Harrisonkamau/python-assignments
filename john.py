import re


def check_string():
    # no need to pass arguments to function if you're not using them
    name = raw_input("Please enter your name: ")

    # open the file using `with` context manager, it'll automatically close the file for you
    with open("john.txt") as data:
        is_there = False
        for line in data:  # iterate over the file one line at a time(memory efficient)
            if re.search(name, line):    # if string found is in current line then print it
                print 'your name is : '+line
                is_there = True
        if not is_there:
            print('Your name cannot be found!')

check_string() # now call the function




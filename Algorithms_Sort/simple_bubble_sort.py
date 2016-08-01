# This is an example of a simple bubble sort algorithm
# create a non-empty list
my_list = [10, -4, 0, 19,35, 98, 73, 104]
length = len(my_list) # length of the list

for item in range(length):
    for j in range(length -1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j] # swap the values
            print my_list


# create a function that takes two lists as arguments
def common_elements(lst1, lst2):
    # make sure the passed arguments are of type list
    lst1 = list(lst1)
    lst2 = list(lst2)

    # create an empty list
    common_list = []

    # sort the lists
    sorted_1 = sorted(lst1)
    sorted_2 = sorted(lst2)

    # iterate through sorted_1 and compare its elements to sorted_2's
    for element in sorted_1:
        for number in sorted_2:
            if number == element:
                common_list.append(number)

    return common_list

print common_elements([1, 2, 3, 45, 51, 7, 19], [11, 21, 17, 19, 7, 51])

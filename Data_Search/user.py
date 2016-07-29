# Instructions
# Create a txt file
# Populate it with any data
# Create a python file
# Prompt the user for input
# if the input is not in the file, then write and save it


def get_course(): # declare a function
    degree = raw_input("Which course would you like to pursue?:")  # prompt the user for input
    courses = open('courses.txt', 'r')  # read through the data
    course_list = courses.readlines()   # save each line in course_list
    courses.close()  # close the file after reading it
    found = False  # create a temp variable and set it to False
    for item in range(0,len(course_list)):
        if degree == course_list[item]:
            print course_list[item]
            print 'welcome to the school of '+course_list[item]
            found = True  # set found to it True if the input matches data in the txt file

        if degree != course_list[item]:
            new_course = open('courses.txt', 'a')
            save_course = new_course.write(degree)  # write the new input and save it
            new_course.close()
    return new_course


print get_course()


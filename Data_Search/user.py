def get_course():
    degree = str(raw_input("Which course would you like to pursue?:"))
    courses = open('courses.txt', 'r')
    courselist = courses.readlines()
    courses.close()
    found = False
    for item in range(0,len(courselist)):
        if degree == int(courselist[item]):
            print 'welcome to the school of '+courselist[item]
            found = True

        if degree != courselist[item]:
            new_course = open('courses.txt')
            save_course = new_course.write()
            new_course.close()


print get_course()


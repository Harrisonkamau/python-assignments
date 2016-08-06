# create a function that takes a number, of any length,
# and converts the numbers to words


# store your numbers in a dictionary
numbers = {'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}


# create the function that will take a number as a parameter
def num_to_word(number):
    num = str(number)  # convert the number to a string for iteration
    string = " "
    for digit in num:
        string += numbers[digit] + " "
    print(string)

print(num_to_word(5450))

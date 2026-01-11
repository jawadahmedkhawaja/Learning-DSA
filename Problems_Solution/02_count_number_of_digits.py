'''
PROBLEM: We have given a number, what we have to do is just count the number of digits given number has.
'''

'''
PLAN

    METHOD-1 (Solution by me and Lecturer)
        - Declare and intialize an count vairable with 0
        - Start a loop while number > 0
        - Increment count vairable
        - In loop divide the number with 10
    METHOD-2: (Solution By Me)
        - Convert the number into string and find the length of string
    METHOD-3: (Solution by Lecturer)
        - Calculate the log10 of number and then add 1 to it.
'''
from math import log10

def count_digits_1(number: int) -> int:
    '''
    Docstring for count_digits_1

    It is a function that will count the number of digits of given number.
    
    :param number: A number whose number of digits are to be counted.
    :type number: int
    :return: Number of digits in given number.
    :rtype: int

    ## Time Complexity

    The time complexity for the function is **O(log10 n)**

    '''
    

    # Declaring a variable to count the digits
    count = 0

    # Loop while number > 0
    while number > 0:

        # Incrementing for each digit
        count += 1

        # Droping last digit from the number
        number = number // 10

    # Returning he number of digits
    return count 


def count_digits_2(number: int) -> int:
    '''
    Docstring for count_digits_2

    It is a function that will count the number of digits of given number.
    
    :param number: A number whose number of digits are to be counted.
    :type number: int
    :return: Number of digits in given number.
    :rtype: int

    ## Time Complexity

    The time complexity for the function is **O(1)**

    '''
    # Returning the number of digits by converting it into string and calculating the length of string
    return len(str(number))

def count_digits_3(number: int) -> int:
    '''
    Docstring for count_digits_1

    It is a function that will count the number of digits of given number.
    
    :param number: A number whose number of digits are to be counted.
    :type number: int
    :return: Number of digits in given number.
    :rtype: int

    ## Time Complexity

    The time complexity for the function is **O(1)**

    '''

    # Calculating the log and adding 1 with it and returning it from the function.
    return int(log10(number) + 1)


if __name__ == "__main__":
    # Counting with method 1
    print(f"Number of digits by using method 1: {count_digits_1(834394)}")

    # Countomg with method 2
    print(f"Number of digits by using method 2: {count_digits_2(834394)}")
    # Counting with method 3
    print(f"Number of digits by using method 3: {count_digits_3(834394)}")
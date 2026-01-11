'''

PROBLEM: We have to extract single digit from a give big number one by one.

'''

'''

PLAN

    - Start a loop till the number get zero and in each iteration divide the number with 100

'''

# Solution 1 (By lecturer and me)
def extract_digits_1(number: int) -> None:
    '''
    Docstring for extract_digits_1
    
    It is a function to extract digits one by one and prints them in reverse order.

    :param number: A number to extract digits from it
    :type number: int
    
    ## Time Complexity

    Time Complexity Time Complexity for given method is **O(log10 n)**

    '''

    # Running loop till number gets zero
    while number > 0:

        # Extracting last digit from given larger digit
        i = number % 10

        # Printing that number
        print(i)

        # Reducing the number by 1 digit
        number = number // 10
        

# Solution 2 (By me)
def extract_digits_2(number: int) -> None:
    '''
    Docstring for extract_digits_2
    
    It is a function to extract digits one by one and prints them in the order as they were.

    :param number: A number to extract digits from it
    :type number: int
    
    ## Time Complexity

    Time Complexity Time Complexity for given method is **O(n)**


    '''

    # Converting te number to string and then iterating over the string for each digit
    for i in str(number):

        # Printing the digit
        print(i)

if __name__ == "__main__":

    # Extracting digit and printing them by using first method
    extract_digits_1(786)

    # Extracting digit and printing them by using first method
    extract_digits_2(786)
   
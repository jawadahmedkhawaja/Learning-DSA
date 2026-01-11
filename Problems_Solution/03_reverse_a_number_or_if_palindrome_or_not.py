'''

PROBLEM: We have to reverse the number and also check if it is palindrome or not.
'''

'''
PLAN
    METHOD-1 (By Lecturer and Me)
        - Reverse the number
        - Compare it with the original number
        - if matched then it will palindrome 
        - else it will not a palindrome
    METHOD-2 (By Me)
        - Convert the number to a string
        - slice it from end
        - Compare sliced string with the original number
        - if matched then it will palindrome 
        - else it will not a palindrome
'''


# METHOD-1
def isPalindrome_1(number: int) -> bool:
    '''
    This function checks for a number is palindrome or not.
    
    :param number: Number to check for palindrome
    :type number: int
    :return: Return true if it is paldindrome else false
    :rtype: bool

    ## Time Complexity

    The time complexity for given method is **O(log10 n)**
    '''

    # Reversing the number
    num = number

    # Variable to store reversed number
    reversed_number =  0

    # Loop for reversing the number
    while num > 0:

        # Adding the number with the previous digit
        reversed_number = (reversed_number * 10) + (num % 10)

        # Droping last digit of given number
        num = num // 10
   
   # Returning true or false based on if number is true or not.
    return reversed_number == number

# METHOD-2
def isPalindrome_2(number: int) -> bool:
    '''
    This function checks for a number is palindrome or not.
    
    :param number: Number to check for palindrome
    :type number: int
    :return: Return true if it is paldindrome else false
    :rtype: bool

    ## Time Complexity
    The time complexity for given method is **O(1)**
    '''

    # Checking and returning the number is palindrome or not
    return str(number)[::-1] == str(number)

if __name__ == "__main__":

    # Checking by method 1
    if(isPalindrome_1(555)):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

    # Checking by method 2
    if(isPalindrome_2(555)):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")
   
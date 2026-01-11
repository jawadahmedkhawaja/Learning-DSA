'''
PROBLEM: Check if a number is palindrome or not
'''


'''
PLAN
    - Count number of digits
    - Extract each digit and calculate its power to number of digits
    - add the digits along with taking there power
    - compare with original number

'''


def isArmstrong(number: int) -> bool:
    '''
    Checks for the number is armstrong number or not.
    
    :param number: Number to check for ArmStrong Number
    :type number: int
    :return: Return true if number is armstrong else return false
    :rtype: bool
    '''
    num = number

    # COUNTING NUMBER OF DIGITS
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    
    num = number
    # Extracting Digits and taking their power
    total = 0 # Variable to store sum
    while num > 0:
        total += (num % 10)**count
        num = num // 10
    
    return total == number



if __name__ == '__main__':
    if (isArmstrong(153)):
        print("Number is Armstrong Number")
    else:
        print("Number is Armstrong number")

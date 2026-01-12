'''
PROBLEM: Retun the factors of given number in a list
'''


'''

PLAN: 
    -  Run the loop till the number given
    - In loop divdide each number with given one
    - Check if remainder is 0 or not
    - if remainder is 0 then it is factor of given number
    - add it to the list
    - else continue

'''

from math import sqrt

def findFactors(number: int) -> list[int]:
    '''
    Returns the list of factors of given **number**
    
    :param number: Number of which to find factors
    :type number: int
    :return: List of factors of given number
    :rtype: list[int]

    ## Time Complexity

    The time complexity for given function is **O(log n)**
    '''
    factors = []

    # Checking if number is 0
    if number == 0:
        return factors
    else:
        # Iterating to find factors
        for i in range(1,number // 2 + 1):
            # If true it is factor
            if number % i == 0:
                # Appedning factor the list
                factors.append(i)
            else:
                continue
        factors.append(number)
    # Returning Factor
    return factors


# Second Method
def factors(number:int) -> list[int]:
    result = []
    for i in range(1,int(sqrt(number)) + 1):
        if number % i == 0:
            result.append(i)
            if number//i != i:
                result.append(number//i)
    result.sort()
    return result
print(findFactors(36))
print(factors(36))
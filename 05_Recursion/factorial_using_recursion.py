'''
PROBLEM: Create a function that will return the factorial of given number (using recursion).
'''


"""
PLAN

    - Just create a base case here we can say the factorial of 0 is 1 and factorial of 1 is 1.
    - After that create a recursive call to the function with n * f(n - 1)
    - That's it
"""

def factorailOfNumber(n):

    # Base Case
    if n == 0 or n == 1:
        return 1
    
    # Recursive Calls
    return n * factorailOfNumber(n-1)

# Calling the function
print(factorailOfNumber(5))
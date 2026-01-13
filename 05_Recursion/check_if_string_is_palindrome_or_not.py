'''

PROBLEM: we have given a string and we have to tell is it palindrome or not.

PALINDROME: A string is said to be a palindrome if we take it reverse and it is equal to the original.

'''


'''
PLAN
    - START
    - Take two variables left and right
    - start a loop and check if the value at the left position of string is equal to the value of string at right position
    - if yes then increment the value of left and decrement the value of right
    - else simply return false
    - STOP
'''

# Method 1
def isPalindrome(s: str) -> bool:
    # Initial Index
    left = 0

    # Last Index
    right = len(s) - 1

    # Traversing each element of the list
    for strng in s:

        # If elements are equal slide he window
        if s[left] == s[right]:
            left += 1
            right -= 1
        
        # IF not equal we already know that one two elements are not same which are must to be same
        else:
            return False
    
    return True


# Method 2
def isPalindrome(s: str, left, right):
    # Base Case 1
    if left >= right:
        return True
    
    # Base Case 2
    if s[left] != s[right]:
        return False
    
    return isPalindrome(s,left + 1, right - 1)
    

print(isPalindrome("mom",0,2))
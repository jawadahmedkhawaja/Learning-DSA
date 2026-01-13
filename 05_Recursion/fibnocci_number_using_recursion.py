'''

PROBLEM: Given a number we have to provide the fibnocci of it

'''

'''

PLAN
    -


'''


def f(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return f(n - 1) + f(n - 2)

print(f(9))
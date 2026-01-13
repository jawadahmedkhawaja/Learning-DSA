
import time
def sendRequest(n):
    for i in range(n+1):
        print(fib(i), end=" ")


def fib(n):
    if n == 1 or n == 0:
        return n
    
    return fib (n - 1) + fib(n - 2)


sendRequest(5)

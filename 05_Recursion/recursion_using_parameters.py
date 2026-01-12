def printSomething(x, n):
    if n == 0:
        return
    printSomething(x,n-1)
    print(x)


printSomething(13,15)
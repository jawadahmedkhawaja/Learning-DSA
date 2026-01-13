def printTable(i, n):
    if i > 10:
        return
    print(f'{n} x {i} = {n * i}')
    printTable(i+1,n)

printTable(1,2)
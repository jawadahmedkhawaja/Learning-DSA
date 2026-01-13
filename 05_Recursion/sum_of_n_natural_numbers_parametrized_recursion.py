def sumNaturalNumbers(sum, i, n):
    if i > n:
        print(sum)
        return
    
    sumNaturalNumbers(sum + i, i+1,n)



sumNaturalNumbers(0,1,10)
def print1ToN(n):
   
    if n<1 :
        return
    
    print1ToN(n-1)
    print(n)


print1ToN(5) 
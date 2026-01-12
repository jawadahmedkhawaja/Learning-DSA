'''

CONSTRAINTS

    - 1 <= n[i] <= 10
    - n can have 10^8 elements
    - m can have 10^8 elements

'''

def printFrequencies(n: list[int,int], m: list[int,int]) -> None:
    for num in m:
        count = 0
        for nu in n:
            if nu == num:
                count += 1
        print(f'{num}: {count}')


# printFrequencies(n=[1,2,3,4,5,4,3,2,1], m=[1,2,3,4,5,6,7,8]) # it can cause a TLE so lets go for optimal solution


# This type of method can be helpful when we have range for numbers
def printFrequencies(n: list[int,int], m: list[int,int]) -> None:
    frequency_list = [0]*10
    for num in n:
        frequency_list[num] += 1
    for num in m:
        if num < 1 or num > 10:
            continue
        else:
            print(f'{num}: {frequency_list[num]}')


printFrequencies(n=[1,2,3,4,5,4,3,2,1], m=[1,2,3,4,5,6,7,8])

# third method can also be uses where first we can store the elements frequency in a dictionary
# This type of method can be helpful when we have no range for numbers
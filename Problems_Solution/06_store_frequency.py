'''

PROBLEM: We have to count the frequency of numbers of each element from given list.

'''


def getFrequency1(nums: list[int]) -> dict[int, int]:
    '''
    Return frequency of each item in a list.
    
    :param nums: List of items to find frequency
    :type nums: list[int]
    :return: Dictionary of each items frequency in key value pairs
    :rtype: dict[int, int]
    '''
    frequencyDict = {}
    for num in nums:
        if num in frequencyDict:
            frequencyDict[num] += 1
        else:
            frequencyDict[num] = 1
    
    return frequencyDict
        

    





def getFrequency2(nums: int) -> dict[int,int]: 
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num,0) + 1

    return frequency

print(getFrequency1(nums=[1,2,3,4,5,5,5,5,5,7,7,7,7,7,6,6,5,4]))
print(getFrequency2(nums=[1,2,3,4,5,5,5,5,5,7,7,7,7,7,6,6,5,4]))
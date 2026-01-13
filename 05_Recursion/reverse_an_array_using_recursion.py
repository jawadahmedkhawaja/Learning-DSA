'''
PROBLEM: Given an array, we have to reverse it.
'''

'''
PLAN

    -
'''

def reverseArray(left, right, array) -> None:
    if left >= right:
        return
    array[left], array[right] = array[right], array[left]

    reverseArray(left=left+1, right=right-1, array=array)
         
        

        
        

array = [1,2,3,4,5,6,7,8,9,10]


reverseArray(0,len(array) - 1, array)

print(array)

        
'''

=> SELECTION SORT
                    A selection is a type of sorting algorithm which is based on

=> ALGORITHM:
            - START
            - Select minimum index
            - Traverse the whole array and compare minimum with all elements and find correct minimum index
            - then place that element at 0th index and so on
            - STOP


'''

def selectionSort(array: list[int]) -> None:
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


array = [1,2,3,4,5,6,7,8,9]
selectionSort(array)
print(array)

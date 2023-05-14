# solving merge sort
# issues to solve:
# 1 - determine if length is <= 1
# 2 - split the array in two with floor division, in case the len of array is odd
# 3 - recursivelly sort and split arrays until len(array) == 1
# 4 - merge them to get the final answer

def mergeSort(array):
    if len(array) > 1:
        n = len(array) // 2 # split the array in 2
        first_subarray = array[:n] # first part
        second_subarray = array[n:] # second part

        mergeSort(first_subarray) # recursivelly sort the first part
        mergeSort(second_subarray) # same for second part

        i = 0 # iterating through the two halves
        j = 0 # iterating through the two halves
        k = 0 # iterating the main array
        while i < len(first_subarray) and j < len(second_subarray):
            if first_subarray[i] < second_subarray[j]:
                array[k] = first_subarray[i]
                i += 1
            else:
                array[k] = second_subarray[j]
                j += 1
            k += 1

        while i < len(first_subarray):
            array[k] = first_subarray[i]
            i += 1
            k +=1
        while j < len(second_subarray):
            array[k] = second_subarray[j]
            j += 1
            k += 1
        return array

        
list = [38, 27, 43, 3, 9, 82, 10, 1]
print(mergeSort(list))
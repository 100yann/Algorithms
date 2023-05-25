def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for x in range(1, len(arr)): # go through all the numbers in the array
        if arr[x] < smallest: # if the current number is smaller than the current smallest number update the "smallest" variable
            smallest = arr[x]
            smallest_index = x
    return smallest_index

def selectionSort(arr):
    newArr = []
    for x in range(len(arr)):
        smallest = findSmallest(arr) # find the smallest number
        newArr.append(arr.pop(smallest)) # remove the smallest number from the original array and add it to the new array
    return newArr

print(selectionSort([5, 3, 6, 2, 10, 12, 1, 18, 22, 15]))

# Time complexity - O(n^2), because for each element in the original array 
# we call the findSmallest function which again iterates through 
# all remaining numbers, essentially n*n
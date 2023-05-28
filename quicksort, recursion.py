# def sum(list):
#  if list == []: # base case
#     return 0
#  return list[0] + sum(list[1:]) # recursive case

# print(sum([2,4,6]))


# def count(list):
#     if list == []: #base case
#         return 0
#     return 1 + count(list[1:]) # recursive case

# print(count([2,4,6]))


# def getMax(list):
#     if len(list) == 2:
#        return list[0] if list[0] > list[1] else list[1]
#     sub_max = getMax(list[1:])
#     return list[0] if list[0] > sub_max else sub_max

# print(getMax([1,3,5,7,9,4,10]))


# QUICKSORT
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)
    


print(quicksort([1, 7, 5, 8, 9, 4, 10, 2, 20]))
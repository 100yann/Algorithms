def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 # if the target is not found within the array

array = list(range(1,101))
x = 35
result = binary_search(array, x)
if result != -1:
    print(f'{x} was found at index {result}')
else:
    print(f'{x} was not found')
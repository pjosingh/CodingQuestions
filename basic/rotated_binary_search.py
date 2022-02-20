

def find_low(arr):

    low = 0
    high = len(arr)-1

    while (low<high):
        mid = int((low+high)/2)
        if (arr[mid] > arr[high]):
            low = mid+1
        else:
            high = mid
    print(low, high)
    return arr[low]


assert find_low([4,5,6,7,0,1,2]) == 0
assert find_low([1,2,4,5,6,7,0]) == 0
assert find_low([0,1,2,4,5,6,7]) == 0
assert find_low([7,0,1,2,4,5,6]) == 0
assert find_low([2,5,0,0,0,0,1,2]) == 0
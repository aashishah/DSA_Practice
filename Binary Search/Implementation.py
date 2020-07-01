#Basic implementation of the Binary Search algorithm. Finding rank / position of a number in a given sorted (ascending / descending) array.

def findRank(x, arr):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return (mid + 1)
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return 0


n = int(input())
arr = list(map(int, input().split(" ")))
if arr[0] > arr[1]:
    arr.sort() #sort to ascending when in descending order
v = int(input())
for _ in range(v):
    print(findRank(int(input()), arr))

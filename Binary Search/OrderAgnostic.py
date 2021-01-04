"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
"""

#CODE:
def orderAgnostic(arr, target):
	length = len(arr)
	ascending = False
	if arr[0] < arr[length - 1]:
		ascending = True

	lo, hi = 0, length - 1
	while lo <= hi:
		mid = lo + (hi - lo) // 2

		if arr[mid] == target:
			return mid

		else:
			if ascending:
				if arr[mid] < target:
					lo = mid + 1
				else:
					hi = mid - 1
			else:
				if arr[mid] < target:
					hi = mid - 1
				else:
					lo = mid + 1

	return -1

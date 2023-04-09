"""
Example 1: Given an array of positive integers nums and an integer k,
find the length of the longest subarray whose sum is less than or equal to k.

Here's some pseudocode illustrating the concept:

function fn(arr):
    left = 0
    for right in [0, arr.length - 1]:
        Do some logic to "add" element at arr[right] to window

        while left < right AND condition from problem not met:
            Do some logic to "remove" element at arr[left] from window
            left++


"""

def find_length_of_longest_subarray(arr : list, k : int):
    left = ans = curr = 0
    for right in range(0, len(arr)):
        curr += arr[right]

        while left < right and curr > k:
            curr -= arr[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
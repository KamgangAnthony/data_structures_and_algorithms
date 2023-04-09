"""
Given a binary array nums and an integer k, return the maximum number
of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

def maximum_consecutive_ones_III(arr: list[int], k: int):
    left = ans = 0
    curr = []

    for right in range(0, len(arr)):
        curr.append(arr[right])

        while curr.count(0) > k:
            curr.pop(0)
            left += 1
        ans = max(ans, right - left + 1)
    return ans

def maximum_consecutive_ones_III2(arr: list[int], k: int):
    left = ans = 0
    curr = 0

    for right in range(0, len(arr)):
        if arr[right] == 0:
            curr += 1

        while curr > k:
            if arr[left] == 0:
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

nums = [0,0,0,0]
k = 0
print(maximum_consecutive_ones_III(nums, k))
"""
Example 3: 713. Subarray Product Less Than K.

Given an array of positive integers nums and an integer k,
return the number of contiguous subarrays where the product of
all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8.
The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Key idea: Whenever you see a problem asking for the number of subarrays,
think of this: at each index, how many valid subarrays end at this index?
Let's split the 8 subarrays by their ending indices:

"""

def number_of_subarrays_less_thanK(nums, k):
    left = 0
    ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]

        while left < right and curr >= k:
            curr /= nums[left]
            left += 1
        ans1 = right - left + 1
        ans += ans1
    return ans

nums = [10, 5, 2, 6]
k = 100
print(number_of_subarrays_less_thanK(nums, k))

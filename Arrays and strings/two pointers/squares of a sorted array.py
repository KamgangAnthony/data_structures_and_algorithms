"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Go through the array,
        square each elt and put it back in position,
        then sort the final array
        and return it
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums"""

        """
        create empty 0's listAns
        Create 2 integers.
        One going from the beginning of the list, the other one going from the end of the list
        Iterate through i in range len(nums) till 0 decreasing
        if abs(actual elt a) > abs(actual elt b):
            add listAns[i] = elt list[a]
            a+=1
        else:
            add listAns[i] = elt list[b]
            b-=1
        i -= 1
        """
        answer = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                answer[i] = nums[right] * nums[right]
                right -= 1
            else:
                answer[i] = nums[left] * nums[left]
                left += 1
        return answer




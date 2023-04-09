"""class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[i + 1] == target:
                if nums[i] == nums[i + 1]:
                    return [nums.index(nums[i]), nums.index(nums[i+1], i+1)]
                return [nums.index(nums[i]), nums.index(nums[i + 1])]

            i += 1


a = Solution()
print(a.twoSum([3,3], 6))"""


class Solution:
    def twoSumSimplified(self, nums: list[int], target: int):

        """Given a sorted array of unique integers and a target integer, return true if there exists a pair of
        numbers that sum to target, false otherwise. This problem is similar to Two Sum. """
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return True
        return False


"""nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 25
a = Solution()
print(a.twoSumSimplified(nums, target))"""

# Given two sorted integer arrays, return an array that combines both of them
# and is also sorted.


def appendsortedarrays(arr1: list[int], arr2: list[int]):
    arr1.sort()
    arr2.sort()
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            ans.append(arr2[j])
        else:
            ans.append(arr2[j])
            ans.append(arr1[i])
        i+=1
        j+=1

    while i < len(arr1):

        ans.append(arr1[i])
        i+=1
    while j < len(arr2):

        ans.append(arr1[j])
        j+=1

    print(ans)

appendsortedarrays([1,4,7,20],[3,5,6])



"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the
elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

1. Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums.
2. Return k.

"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                nums[i] = ''
        while '' in nums:
            nums.remove('')

        return len(nums)


assert Solution().removeDuplicates([1, 1, 2]) == 2
assert Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 4, 4]) == 5

"""
Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            freeze_num = num
            new_nums = nums[:]
            new_nums.remove(freeze_num)
            for new_num in new_nums:
                if freeze_num + new_num == target:
                    if nums.count(new_num) == 1:
                        return [nums.index(freeze_num), nums.index(new_num)]
                    else:
                        current_index = -1
                        temp_index = -1
                        for i in nums:
                            temp_index += 1
                            if i == new_num:
                                current_index = temp_index
                        return [nums.index(freeze_num), current_index]


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

"""


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_lst = nums1 + nums2
        total_lst.sort()

        if len(total_lst) % 2:
            mid_index = len(total_lst) // 2
            median = total_lst[mid_index]
        else:
            after_mid_index = int(len(total_lst) / 2)
            previous_mid_index = after_mid_index - 1
            median = (total_lst[previous_mid_index] + total_lst[after_mid_index]) / 2

        return median


assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

"""
Given an integer x, return true if x is a palindrome , and false otherwise.

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


assert Solution().isPalindrome(121) is True
assert Solution().isPalindrome(-121) is False
assert Solution().isPalindrome(10) is False

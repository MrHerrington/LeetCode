"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""


class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        if string[0] == '-':
            num = -abs(int(string[:0:-1]))
        else:
            num = int(string[::-1])

        if -2 ** 31 <= num <= 2 ** 31 - 1:
            return num
        else:
            return 0


assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(120) == 21
assert Solution().reverse(1534236469) == 0

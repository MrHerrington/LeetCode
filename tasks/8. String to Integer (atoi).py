"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    1. Whitespace: Ignore any leading whitespace (" ").
    2. Signedness: Determine the sign by checking if the next character is '-' or '+',
    assuming positivity is neither present.
    3. Conversion: Read the integer by skipping leading zeros until a non-digit character is
    encountered or the end of the string is reached. If no digits were read, then the result is 0.
    4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
    then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        negative = None
        positive = None
        digits = ''

        for i in s:
            if i.isspace() and not negative and not positive and not digits:
                continue
            elif i == '-' and not digits and not negative and not positive:
                negative = True
            elif i == '+' and not digits and not positive and not negative:
                positive = True
            elif i.isdigit() and int(i) == 0 and not digits:
                digits += i
            elif i.isdigit() and int(i) == 0 and digits or i.isdigit() and int(i) > 0:
                digits += i
                if digits[0] == '0':
                    digits = digits[1:]
            else:
                break

        if not digits:
            digits = 0

        if negative:
            num = -int(digits)
        else:
            num = int(digits)

        if num < -2 ** 31:
            num = -2 ** 31
        elif num >= 2 ** 31:
            num = 2 ** 31 - 1

        return num


assert Solution().myAtoi('42') == 42
assert Solution().myAtoi(' -042') == -42
assert Solution().myAtoi('1337c0d3') == 1337
assert Solution().myAtoi('0-1') == 0
assert Solution().myAtoi('words and 987') == 0
assert Solution().myAtoi('') == 0
assert Solution().myAtoi('+1') == 1
assert Solution().myAtoi('+-12') == 0
assert Solution().myAtoi('21474836460') == 2147483647
assert Solution().myAtoi('2147483648') == 2147483647
assert Solution().myAtoi('  +  413') == 0
assert Solution().myAtoi(' ++1') == 0

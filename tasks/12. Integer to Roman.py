"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX.
Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

"""


class Solution:
    def intToRoman(self, num: int) -> str:
        dct = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        
        roman_res=''

        while num:
            for k, v in dct.items():
                if num // v:
                    roman_res += k
                    num -= v
                    break

        return roman_res


assert Solution().intToRoman(3) == 'III'
assert Solution().intToRoman(4) == 'IV'
assert Solution().intToRoman(9) == 'IX'
assert Solution().intToRoman(58) == 'LVIII'
assert Solution().intToRoman(1994) == 'MCMXCIV'
assert Solution().intToRoman(3749) == 'MMMDCCXLIX'

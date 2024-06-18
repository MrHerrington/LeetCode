"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR".

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        field = {}
        max_col = 0
        max_row = 0
        col = 0
        row = -1
        increase = True
        if numRows == 1:
            return s
        else:
            for i in s:
                if increase and row + 1 < numRows:
                    row += 1
                else:
                    if row - 1 > -1:
                        col += 1
                        row -= 1
                        increase = False
                    else:
                        # col += 1
                        row += 1
                        increase = True

                field[col, row] = i
                if row > max_row:
                    max_row = row
                if col > max_col:
                    max_col = col

            matrix = [['' for _ in range(max_col + 1)] for _ in range(max_row + 1)]

            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if (j, i) in field:
                        matrix[i][j] = field[j, i]

            return ''.join(map(lambda x: ''.join(x), matrix))


assert Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert Solution().convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
assert Solution().convert('A', 1) == 'A'
assert Solution().convert('ABC', 1) == 'ABC'

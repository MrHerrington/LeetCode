"""
Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*' where:
    1. '.' Matches any single character.
    2. '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]


assert Solution().isMatch('aa', 'a') is False
assert Solution().isMatch('aab', 'c*a*b') is True
assert Solution().isMatch('abcd', 'd*') is False
assert Solution().isMatch('ab', '.*c') is False
assert Solution().isMatch('aaa', 'aaaa') is False
assert Solution().isMatch('aaa', 'ab*a') is False
assert Solution().isMatch('aaa', 'ab*a*c*a') is True

"""
Given a string s, return the longest palindromic substring in s.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sequence = ''
        current_sequence = []

        for i in range(len(s)):
            current_sequence.clear()
            current_sequence.append(s[i])

            for j in range(i + 1, len(s) + 1):
                temp_sequence = s[i:j]
                if temp_sequence == temp_sequence[::-1] and len(temp_sequence) > len(longest_sequence):
                    longest_sequence = ''.join(temp_sequence)

        return longest_sequence


assert Solution().longestPalindrome("babad") == "bab"
assert Solution().longestPalindrome("cbbd") == "bb"
assert Solution().longestPalindrome("aacabdkacaa") == "aca"
assert Solution().longestPalindrome("aaaa") == "aaaa"

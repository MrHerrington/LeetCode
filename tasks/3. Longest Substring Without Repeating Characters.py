"""
Given a string s, find the length of the longest substring without repeating characters.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_sequence = []
        for i in range(len(s)):
            left_i = i
            right_i = i
            current_sequence.clear()
            current_sequence.append(s[i])
            while left_i - 1 > 0 and s[left_i - 1] not in current_sequence:
                current_sequence.append(s[left_i - 1])
                left_i -= 1
            while right_i + 1 < len(s) and s[right_i + 1] not in current_sequence:
                current_sequence.append(s[right_i + 1])
                right_i += 1
            max_length = max(max_length, len(current_sequence))

        return max_length


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring(" ") == 1
assert Solution().lengthOfLongestSubstring("aab") == 2
assert Solution().lengthOfLongestSubstring("dvdf") == 3

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        temp_prefix = ''
        for i in range(min(map(len, strs))):
            add = True
            for word in strs:
                if strs.index(word) == 0:
                    temp_prefix = word[i]
                else:
                    if word[i] != temp_prefix:
                        add = False
                        break
            if not add:
                break
            else:
                common_prefix += temp_prefix

        return common_prefix


assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert Solution().longestCommonPrefix(["cir", "car"]) == "c"

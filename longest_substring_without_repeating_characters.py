# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_len = 0
        for c in s:
            if c in substring:
                index = substring.index(c)
                del substring[0:index + 1]
            substring.append(c)
            max_len = max(max_len, len(substring))
        return max_len

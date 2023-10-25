# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        strs = list(set(strs))
        first_string = strs[0]

        if len(strs) == 1:
            return first_string

        for i in range(1, len(first_string) + 1):
            sliced_elements = slice(i)
            for s in strs:
                if first_string[sliced_elements] != s[sliced_elements]:
                    return prefix
            prefix = first_string[sliced_elements]
        return prefix

# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        longest = 1
        STR_LEN = len(s)

        def lp(left: int, right: int, result: str, longest: int):
            while left >= 0 and right < STR_LEN and s[left] == s[right]:
                substring = s[left:right + 1]

                if len(substring) > longest and substring == substring[::-1]:
                    result = substring
                    longest = len(substring)

                left -= 1
                right += 1

            return result, longest

        for i in range(STR_LEN):
            start, end = i, i  # for even
            tmp_result, tmp_longest = lp(start, end, result, longest)

            if tmp_longest > longest:
                result = tmp_result
                longest = tmp_longest

            tmp_result, tmp_longest = lp(start, end + 1, result, longest)  # for odd

            if tmp_longest > longest:
                result = tmp_result
                longest = tmp_longest

        return result

# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        nums = set(nums)

        for n in nums:
            if n - 1 not in nums:
                start = n
                while start in nums:
                    start += 1
                longest = max(start - n, longest)

        return longest

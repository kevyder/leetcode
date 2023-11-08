# 169. Majority Element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        unique_nums = set(nums.copy())
        size = len(nums) // 2

        for n in unique_nums:
            if nums.count(n) > size:
                return n

# 268. Missing Number
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if 0 not in nums:
            return 0

        elements = len(nums)

        result = elements * (elements + 1) // 2

        for n in nums:
            result -= n

        if not result:
            return elements

        return result

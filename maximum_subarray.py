# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_sum = 0
        max_result = nums[0]

        for n in nums:
            if max_sum < 0:
                max_sum = 0

            max_sum += n

            if max_sum > max_result:
                max_result = max_sum

        return max_result

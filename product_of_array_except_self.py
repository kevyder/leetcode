# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_size = len(nums)
        left = [1] * nums_size
        right = left.copy()
        answers = left.copy()

        for i in reversed(range(1, nums_size)):
            right[i - 1] = right[i] * nums[i]

        for i in range(nums_size - 1):
            left[i + 1] = left[i] * nums[i]

        for index in range(nums_size):
            answers[index] = right[index] * left[index]

        return answers

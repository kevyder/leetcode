# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1
        min_result = nums[start]

        while start <= end:

            if nums[start] < nums[end]:
                min_result = min(min_result, nums[start])
                break

            middle_point = (start + end) // 2
            min_result = min(min_result, nums[middle_point])

            if nums[middle_point] >= nums[start]:
                start = middle_point + 1
            else:
                end = middle_point - 1

        return min_result

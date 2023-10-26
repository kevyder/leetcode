# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        start, end = 0, len(nums)

        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return end
        elif nums[-1] == target:
            return end - 1

        # Use binary search
        while True:
            index = (start + end) // 2

            if nums[index] == target or (nums[index - 1] < target and nums[index] > target):
                return index

            if nums[index] < target:
                start = index + 1
            else:
                end = index


# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        indices_to_remove = []
        correction = 0

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                indices_to_remove.append(i)

        for index in indices_to_remove:
            nums.pop(index - correction)
            correction += 1

        return len(nums)

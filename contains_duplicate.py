# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

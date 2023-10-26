# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for number in nums1[m:]:
            nums1.remove(number)

        nums1.extend(nums2[slice(n)])
        nums1.sort()

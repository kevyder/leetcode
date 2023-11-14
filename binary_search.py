# 704. Binary Search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)

        while True:
            index = (start + end) // 2
            num = nums[index]

            if num == target:
                return index
            elif num < target:
                start = index + 1
            else:
                end = index

            if start == end:
                return -1

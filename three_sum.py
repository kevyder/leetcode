# 15. 3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> set[tuple[int]]:
        length = len(nums)
        results = set()
        nums.sort()

        for i in range(length):
            start, end = i + 1, length - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while start < end:
                result = nums[i] + nums[start] + nums[end]
                if result == 0:
                    results.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif result < 0:
                    start += 1
                else:
                    end -= 1

        return results

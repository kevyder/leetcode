# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        original_nums = nums.copy()
        nums_len = len(original_nums)

        def backtracking(current_index, numbers):
            if not any(numbers):
                return

            current_number = numbers.pop(0)

            for n in numbers:
                if current_number + n == target:
                    index = original_nums.index(n, current_index + 1, nums_len)
                    indices.extend([current_index, index])

            backtracking(current_index + 1, numbers)

        backtracking(0, nums)
        sum_indices = list(set(indices))
        return sum_indices

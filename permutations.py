# 46. Permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        elements_len = len(nums)
        result = []

        if elements_len == 1:
            return [nums.copy()]

        for i in range(0, elements_len):
            num = nums.pop(0)  # use backtracking
            permutations = self.permute(nums)  # use recursion

            for permutation in permutations:
                permutation.append(num)

            result.extend(permutations)
            nums.append(num)

        return result

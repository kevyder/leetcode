class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = []

        def dfs(current_index: int, subset: list = []):
            if current_index >= len(nums):
                results.append(subset.copy())
                return

            subset.append(nums[current_index])
            dfs(current_index + 1, subset)

            subset.pop()
            dfs(current_index + 1, subset)

        dfs(0)

        return results

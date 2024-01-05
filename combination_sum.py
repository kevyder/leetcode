# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates_size = len(candidates)

        def dfs(current_index: int, current_combination: list = [], total: int = 0) -> None:
            if total == target:
                results.append(current_combination.copy())
                return

            if current_index >= candidates_size or total > target:
                return

            current_number = candidates[current_index]

            # decision tree repeating number
            current_combination.append(current_number)
            dfs(current_index, current_combination, total + current_number)

            # decision tree with different number
            current_combination.pop()
            dfs(current_index + 1, current_combination, total)

        dfs(0)

        return results

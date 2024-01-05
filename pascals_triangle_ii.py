# 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]  # base case

        if rowIndex == 0:
            return result

        for current_n_rows in range(2, rowIndex + 2):
            new_row = [1] * current_n_rows

            for pointer in range(len(result) - 1):
                new_row[pointer + 1] = result[pointer] + result[pointer + 1]

            result = new_row

        return result

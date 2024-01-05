# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]  # base case

        if numRows == 1:
            return result

        for current_n_rows in range(2, numRows + 1):
            new_row = [1] * current_n_rows
            last_row = result[-1]

            for pointer in range(len(last_row) - 1):
                new_row[pointer + 1] = last_row[pointer] + last_row[pointer + 1]

            result.append(new_row)

        return result

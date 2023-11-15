# 74. Search a 2D Matrix


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        size = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False

            start, end = 0, size

            while True:
                index = (start + end) // 2
                number = matrix[i][index]

                if number == target:
                    return True

                if start == end:
                    break
                elif number > target:
                    end = index
                else:
                    start = index + 1

        return False

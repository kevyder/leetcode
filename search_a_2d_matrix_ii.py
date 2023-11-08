# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        size = len(matrix[0])

        for m in range(len(matrix)):
            start, end = 0, size

            if matrix[m][0] > target:
                return False

            while True:
                index = (start + end) // 2
                number = matrix[m][index]

                if number == target:
                    return True

                if number < target:
                    start = index + 1
                else:
                    end = index

                if start == end:
                    break

        return False

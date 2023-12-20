# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        start, end = 0, len(height) - 1
        max_area = 0

        while start < end:
            area = (end - start) * min(height[start], height[end])
            max_area = max(area, max_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

# Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        multiplier, column = 1, 0
        columnTitle = columnTitle.lower()

        for char in columnTitle[::-1]:
            column += (ord(char) - 96) * multiplier
            multiplier *= 26

        return column

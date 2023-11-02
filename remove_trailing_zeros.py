# 2710. Remove Trailing Zeros From a String
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = list(num)
        for n in num[::-1]:
            if n != "0":
                return "".join(num)
            num.pop()

# 1957. Delete Characters to Make Fancy String
class Solution:
    def makeFancyString(self, s: str) -> str:
        new_string = []
        for i, c in enumerate(s):
            new_string.append(c)
            if len(new_string) >= 3 and (c == new_string[-1] == new_string[-2] == new_string[-3]):
                new_string.pop()
        return "".join(new_string)


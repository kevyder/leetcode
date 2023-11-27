# 20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {")": "(", "}": "{", "]": "["}

        close_chars = close_to_open.keys()

        for c in s:
            if c in close_chars:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not any(stack)

# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        digits_length = len(digits)
        T9 = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(index: int, current_string: str) -> None:
            if index == digits_length:
                result.append(current_string)
                return

            for char in T9[digits[index]]:
                backtrack(index + 1, f"{current_string}{char}")

        if digits:
            backtrack(0, "")

        return result

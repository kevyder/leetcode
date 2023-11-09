# 1137. N-th Tribonacci Number


class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]

        if n <= 2:
            return seq[n]

        for i in range(3, n + 1):
            next_element = sum(seq)
            seq.append(next_element)
            seq.pop(0)

        return seq[-1]

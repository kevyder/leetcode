# 347. Top K Frequent Elements


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        return list(sorted_freq.keys())[slice(k)]

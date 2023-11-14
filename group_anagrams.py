# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in results.keys():
                results[sorted_word].append(word)
            else:
                results[sorted_word] = [word]

        return list(results.values())

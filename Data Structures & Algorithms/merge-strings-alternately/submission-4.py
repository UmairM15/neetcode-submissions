class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            i = 0
            minLen = min(len(word1), len(word2))
            res = []

            while i < minLen:
                res.append(word1[i])
                res.append(word2[i])
                i += 1

            res.append(word2[i:])
            res.append(word1[i:])

            return "".join(res)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        minLen = min(len(word1), len(word2))
        res = ""

        while i < minLen:
            res += word1[i]
            res += word2[i]
            i += 1

        if len(word1) < len(word2):
            res += word2[i:]
        else:
            res += word1[i:]

        return res
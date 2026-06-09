from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1
        need = len(tCount)

        minLen = float("inf")
        minL, minR = 0, len(s)
        sCount = defaultdict(int)
        l = cur = 0
        for r in range(len(s)):
            rightChar = s[r]
            sCount[rightChar] += 1
            if sCount[rightChar] == tCount[rightChar] and tCount[rightChar] != 0:
                cur += 1
            while cur == need:
                leftChar = s[l]
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    minL = l
                    minR = r
                if sCount[leftChar] == tCount[leftChar] and tCount[leftChar] != 0:
                    cur -= 1
                sCount[leftChar] -= 1
                l += 1

        return "" if minLen == float("inf") else s[minL:minR + 1]

        
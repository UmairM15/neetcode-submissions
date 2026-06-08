from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1Count = defaultdict(int)
        for c in s1:
            c1Count[c] += 1
        c2Count = defaultdict(int)
        l = 0
        cur, need = 0, len(c1Count)
        for r in range(len(s2)):
            rightChar = s2[r]
            c2Count[rightChar] += 1
            if c2Count[rightChar] == c1Count[rightChar]:
                cur += 1
            elif c2Count[rightChar] == c1Count[rightChar] + 1:
                cur -= 1
            if r - l + 1 > len(s1):
                leftChar = s2[l]
                if c2Count[leftChar] == c1Count[leftChar]:
                    cur -= 1
                c2Count[leftChar] -= 1
                if c2Count[leftChar] == c1Count[leftChar]:
                    cur += 1
                l += 1
            if cur == need:
                return True
        return False
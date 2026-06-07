class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        l = r = 0
        maxLen = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                maxLen = max(maxLen, r - l)
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                
        return max(maxLen, r - l)
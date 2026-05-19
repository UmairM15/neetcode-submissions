class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        prefix = ""

        for i in range(len(first)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != first[i]:
                    return prefix
            prefix += first[i]

        return prefix
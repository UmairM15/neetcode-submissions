class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedStrs = strs
        sortedStrs.sort(key=len)
        prefix = ""

        for i in range(len(sortedStrs[0])):
            for j in range(1, len(sortedStrs)):
                if (sortedStrs[0])[i] != (sortedStrs[j])[i]:
                    return prefix
            prefix += (sortedStrs[0])[i]

        return prefix
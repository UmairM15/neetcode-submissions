class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            found = False

            for ang in groups:
                if self.isAnagram(s, ang):
                    groups[ang].append(s)
                    found = True
                    break
            if not found:
                groups[s] = list([s])
        
        return list(groups.values())
        
    def isAnagram(self, str1, str2):
        seen = {}
        for c in str1:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        
        for c in str2:
            if c not in seen:
                return False
            seen[c] -= 1
            if seen[c] == 0:
                del seen[c]
        
        return not seen
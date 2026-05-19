class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        str = s
        for c in t:
            if c in str:
                str = str.replace(c, '', 1)
            else:
                return False
        
        return True
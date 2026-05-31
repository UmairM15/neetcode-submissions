class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(first, second):
            s = first + second
            i, j = 0, len(s) - 1

            while i < j:
                if not s[i].isalnum():
                    i += 1
                    continue
                if not s[j].isalnum():
                    j -= 1
                    continue

                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1
            
            return True

        for i in range(len(s)):
            if isPalindrome(s[:i], s[i+1:]):
                return True
        
        return False
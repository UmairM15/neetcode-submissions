class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0
        for c in s:
            if c == "[":
                stack.append((cur, num))
                cur = ""
                num = 0
            elif c == "]":
                prev, num = stack.pop()
                cur = prev + num * cur
                num = 0
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                cur += c
        return cur
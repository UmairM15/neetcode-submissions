class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                chars = []
                multiplier = 0
                decimalPlace = 1
                while stack[-1] != "[":
                    chars.append(stack.pop())
                substring = "".join(reversed(chars))
                stack.pop() # remove "["
                while stack and stack[-1].isnumeric():
                    multiplier += int(stack.pop()) * decimalPlace
                    decimalPlace *= 10
                stack.append(multiplier * substring)
            else:
                stack.append(c)
        return "".join(stack)
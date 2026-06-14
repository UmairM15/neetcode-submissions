class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and a < 0:
                while stack and stack[-1] * a < 0 and abs(stack[-1]) < abs(a):
                    stack.pop()
                if stack and stack[-1] > 0:
                    if stack[-1] == -a:
                        stack.pop()
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
                    
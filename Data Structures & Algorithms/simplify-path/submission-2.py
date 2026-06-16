class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [""]
        pathList = path.split("/")
        i = 0
        print(pathList)
        for c in pathList:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(c)
            print(stack)
        return "/".join(stack) if len(stack) > 1 else "/"
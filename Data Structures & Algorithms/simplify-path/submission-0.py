class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        dirs = path.split("/")

        for d in dirs:
            if d == "":
                continue
            elif stack and d == "..":
                stack.pop()
            elif not stack and d == "..":
                continue
            else:
                stack.append(d)
        
        return "/" + "/".join(stack)
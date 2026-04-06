class Solution:
    def checkValidString(self, s: str) -> bool:
        star = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                elif star > 0:
                    star -= 1
                else:
                    return False
            elif c == "*":
                star += 1

        if len(stack) <= star:
            return True

        return False
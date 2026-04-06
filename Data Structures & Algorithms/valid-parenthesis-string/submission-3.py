class Solution:
    def checkValidString(self, s: str) -> bool:
        sStack = []
        lStack = []

        for i, c in enumerate(s):
            if c == "(":
                lStack.append(i)
            elif c == ")":
                if lStack:
                    lStack.pop()
                elif sStack:
                    sStack.pop()
                else:
                    return False
            elif c == "*":
                sStack.append(i)

        if len(lStack) > len(sStack):
            return False

        while lStack:
            rMostL = lStack.pop()
            if sStack:
                rMostS = sStack.pop()
                if rMostL > rMostS:
                    return False
            else:
                return False

        return True
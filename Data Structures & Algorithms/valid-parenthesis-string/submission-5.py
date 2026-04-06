class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        left = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif c == "*":
                star.append(i)

        while left and star:
            if left[-1] > star[-1]:
                    return False
            left.pop()
            star.pop()

        return False if left else True
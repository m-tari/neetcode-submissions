class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        k, cur = "", ""
        numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        i, n = 0, len(s)

        while i < n:

            if s[i] in numbers:
                k += s[i]

            elif s[i] == "[":
                numStack.append(k)
                strStack.append(cur)
                cur = ""
                k = ""

            elif s[i] == "]":
                level_cur = strStack.pop()
                k = numStack.pop()
                cur = level_cur + int(k) * cur
                k = ""

            else:
                cur += s[i]

            i += 1

        return cur
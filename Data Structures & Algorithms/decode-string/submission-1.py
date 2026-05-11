class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        cur = ""
        numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        i, n = 0, len(s)

        while i < n:

            if s[i] in numbers:
                k = ""
                while s[i] in numbers:
                    k += s[i]
                    i += 1
                numStack.append(int(k))
                continue

            elif s[i] == "[":
                strStack.append(cur)
                cur = ""

            elif s[i] == "]":
                level_cur = strStack.pop()
                k = numStack.pop()
                cur = level_cur + k * cur
                
            else:
                cur += s[i]

            i += 1

        return cur
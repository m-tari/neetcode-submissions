class Solution:
    def romanToInt(self, s: str) -> int:
        symValue = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        if n == 1:
            return symValue[s]

        res = symValue[s[0]]
        for i in range(1, n):
            curr = s[i]
            prev = s[i-1]

            if symValue[curr]<= symValue[prev]:
                res += symValue[curr]
            else:
                res += (symValue[curr] - symValue[prev]) - symValue[prev]

        return res
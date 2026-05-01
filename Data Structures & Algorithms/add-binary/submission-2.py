class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0

        while i >=0 or j >=0 or carry:
            digitA, digitB = 0, 0

            if i >= 0:
                digitA = int(a[i])
                i -= 1

            if j >=0:
                digitB = int(b[j])
                j -= 1

            total = digitA + digitB + carry
            num = total % 2
            carry = total // 2
            res.append(str(num))

        res.reverse()
        return "".join(res)
        
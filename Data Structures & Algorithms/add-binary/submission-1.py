class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0

        while i >=0 or j >=0 or carry:
            num1, num2 = 0, 0

            if i >= 0:
                num1 = int(a[i])
                i -= 1

            if j >=0:
                num2 = int(b[j])
                j -= 1

            num = (num1 + num2 + carry) % 2
            carry = (num1 + num2 + carry) // 2
            res.append(str(num))

        res.reverse()
        return "".join(res)
        
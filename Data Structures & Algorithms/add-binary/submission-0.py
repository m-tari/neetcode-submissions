class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        if len(b) > len(a):
            a, b = b, a

        a = a[::-1]    
        b = b[::-1]
        carry = 0
        for i in range(len(b)):
            if a[i] == "0" and b[i] == "0":
                if carry:
                    res.append("1")
                    carry = 0
                else:
                    res.append("0")
            elif a[i] == "1" and b[i] == "0":
                if carry:
                    res.append("0")
                else:
                    res.append("1")
            elif a[i] == "0" and b[i] == "1":
                if carry:
                    res.append("0")
                else:
                    res.append("1")
            elif a[i] == "1" and b[i] == "1":
                if carry:
                    res.append("1")
                else:
                    res.append("0")
                    carry = 1

        for j in range(len(b), len(a)):
            if carry:
                if a[j] == "0":
                    res.append("1")
                    carry = 0
                else:
                    res.append("0")
            else:
                res.append(a[j])

        if carry:
            res.append("1")

        return "".join(res[::-1])
        
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        items = ""
        sizes = []
        for item in strs:
            l = len(item)
            sizes.append(str(l))
            items += item

        res = ",".join(sizes) + "#" + items
        return  res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0
        l = ""
        sizes = []
        while s[i]  != "#":
            if  s[i] != ",":
                l += s[i]
            else:
                sizes.append(int(l))
                l = ""
            i += 1

        sizes.append(int(l))
        j = i + 1  ## For # case
        for size in sizes:
            res.append(s[j: j + size])
            j += size

        return res
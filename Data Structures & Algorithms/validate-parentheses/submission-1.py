class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if char in mapping:
                if stack and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
        
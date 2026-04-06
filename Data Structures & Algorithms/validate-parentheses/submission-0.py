class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if stack and mapping[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
            print(stack)
        return True if not stack else False
        
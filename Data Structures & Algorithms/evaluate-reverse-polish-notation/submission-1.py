class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "/", "*"}
        stack = []

        for t in tokens:
            if t not in operands:
                stack.append(t)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num1 - num2
                elif t == '*':
                    res = num1 * num2
                elif t == '/':
                    res = int(num1 / num2)
                stack.append(res)

        return stack[0]


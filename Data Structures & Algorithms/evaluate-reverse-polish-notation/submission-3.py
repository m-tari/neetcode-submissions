class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "/", "*"}
        stack = []

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == '+':
                    res = num2 + num1
                elif t == '-':
                    res = num2 - num1
                elif t == '*':
                    res = num2 * num1
                elif t == '/':
                    res = int(num2 / num1)
                stack.append(res)

        return stack[0]


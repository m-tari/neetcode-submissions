class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []
        # l number of "(" in stack
        # r number of ")" in stack

        def dfs(stack, l, r):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return

            if l < n:
                stack.append("(")
                dfs(stack, l+1, r)
                stack.pop()
            if l > r:
                stack.append(")")
                dfs(stack, l, r + 1)
                stack.pop()

        dfs(stack, 0, 0)
        return res
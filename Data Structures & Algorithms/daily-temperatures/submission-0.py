class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        stack = []  # [idx, temp] pair

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIdx, stackT = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append([i, t])

        return result
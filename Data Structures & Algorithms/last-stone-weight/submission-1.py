class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def smash(stones):
            stones.sort()
            if len(stones) == 1:
                return stones[0]
            elif len(stones) == 0:
                return 0

            num1 = stones.pop()
            num2 = stones.pop()
            if num1 != num2:
                stones.append(abs(num1 - num2))
            return smash(stones)
                
        return smash(stones)
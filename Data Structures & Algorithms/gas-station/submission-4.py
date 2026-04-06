class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        i = 0
        n = len(gas)
        idx = 0

        for i in range(n):
         total += gas[i] - cost[i]
         if gas[i] > cost[i]:
            flip = False
         if total <= 0:
            total = 0
            idx = i + 1 if i != n - 1 else 0

        return idx
        
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def dfs(i):
            if i == len(days):
                return 0

            res = float('inf')
            j = i
            for d, c in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                # “Among all ticket choices (1, 7, 30 days), keep the cheapest total cost.”
                res = min(res,  c + dfs(j))

            return res

        return dfs(0)


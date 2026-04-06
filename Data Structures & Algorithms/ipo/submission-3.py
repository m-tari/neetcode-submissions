class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        curr_cap = w
        finished = set()
        for proj in range(k):
            feas_proj = [idx for idx, cap in enumerate(capital) if cap <= curr_cap and idx not in finished]
            if not feas_proj:
                return curr_cap
            feas_proj_profits = [profits[idx] for idx in feas_proj]
            max_prof = max(feas_proj_profits)

            max_prof_idx  = feas_proj_profits.index(max_prof)
            max_cap_idx = feas_proj[max_prof_idx]
            curr_cap += max_prof
            finished.add(max_cap_idx)

        return curr_cap
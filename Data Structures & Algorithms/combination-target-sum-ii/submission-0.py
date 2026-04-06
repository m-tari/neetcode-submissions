class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res =[]
        candidates.sort()

        def dfs(i, rem, comb):
            if rem == 0:
                res.append(comb.copy())
                return

            if rem < 0 or i > len(candidates):
                return

            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                if rem - candidates[idx] < 0:
                    break

                comb.append(candidates[idx])
                dfs(idx + 1, rem - candidates[idx], comb)
                comb.pop()

            return

        dfs(0, target, [])

        return res
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        candidate = r

        while l <= r:
            m = (l + r) // 2
            cur_w = 0
            cur_days = 1

            for w in weights:
                if cur_w + w <= m:
                    cur_w += w
                else:
                    cur_w = w
                    cur_days += 1

                if cur_days > days:
                    break

            if cur_days <= days:
                r = m - 1
                candidate = min(candidate, m)
            else:
                l = m + 1
            
        return candidate

    # 2 4  6 1  3  10

    # sum = 26 -> / 4 -> 6... -> 7   best if we divide by days

    # min capacity  = 10 (max of array)
    # max capacity = 26 (sum of the weights)

    # do binary search
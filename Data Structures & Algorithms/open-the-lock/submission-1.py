from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocks = set(deadends)
        visit  = set(["0000"])
        q = deque(["0000"])
        turn = 0
        nei_map = { 
            "0": ["1", "9"],
            "1": ["2", "0"],
            "2": ["3", "1"],
            "3": ["4", "2"],
            "4": ["5", "3"],
            "5": ["6", "4"],
            "6": ["7", "5"],
            "7": ["8", "6"],
            "8": ["9", "7"],
            "9": ["0", "8"],
            }

        while q:
            for _ in range(len(q)):
                val = q.popleft()

                if val in blocks:
                    continue

                if val == target:
                    return turn

                for i in range(4):
                    for move in nei_map[val[i]]:
                        valList = list(val)
                        valList[i] = move
                        nei = "".join(valList)

                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            turn += 1

        return -1
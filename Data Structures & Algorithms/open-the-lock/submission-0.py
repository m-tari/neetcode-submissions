from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocks = set(deadends)
        visit  = set()
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
            for i in range(len(q)):
                val = q.popleft()
                if val in blocks:
                    continue

                if val == target:
                    return turn

                neighbours = []
                for i in range(4):
                    valList = [ch for ch in val]
                    valList[i] = nei_map[val[i]][0]
                    neighbours.append("".join(valList))
                    valList[i] = nei_map[val[i]][1]
                    neighbours.append("".join(valList))

                for nei in neighbours:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                        
            turn += 1

        return -1
class CountSquares:

    def __init__(self):
        self.points = {}  # (x,y) -> frequency
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) +  1

    def count(self, point: List[int]) -> int:
        res = 0
        xq, yq = point
        for x, y in self.points:
            if (xq - x)**2 == (yq - y)**2 and xq != x :
                if (xq, y) in self.points and (x, yq) in self.points:
                    res += self.points[(xq, y)] * self.points[(x, yq)] * self.points[(x, y)]
        
        return res
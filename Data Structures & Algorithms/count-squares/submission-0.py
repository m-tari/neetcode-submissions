from collections import defaultdict

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
            if (xq - x)**2 == (yq - y)**2 :
                # query at bottom right
                if x < xq and y > yq:
                    if (xq, y) in self.points and (x, yq) in self.points:
                        res += self.points[(xq, y)] * self.points[(x, yq)]
                # query at bottom left
                if x > xq and y > yq:
                    if (x, yq) in self.points and (xq, y) in self.points:
                        res += self.points[(x, yq)] * self.points[(xq, y)]
                # query at top left
                if x > xq and y < yq:
                    if (x, yq) in self.points and (xq, y) in self.points:
                        res += self.points[(x, yq)] * self.points[(xq, y)]
                # query at top right
                if x < xq and y < yq:
                    if (xq, y) in self.points and (x, yq) in self.points:
                        res += self.points[(xq, y)] * self.points[(x, yq)]
        
        return res
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        first, second, third = False, False, False
        x, y, z = target
        for a, b, c in triplets:
            if a == x and b <= y and c <= z :
                first = True
            if a <= x and b == y and c <= z:
                second = True
            if a <= x and b <= y and c == z:
                third = True

        return first == second == third == True
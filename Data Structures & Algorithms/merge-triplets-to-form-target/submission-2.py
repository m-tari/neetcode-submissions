class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        first, second, third = False, False, False
        x, y, z = target

        for a, b, c in triplets:
            # skip triplets that overshoot the target in any coordinate
            if a > x or b > y or c > z:
                continue

            if a == x  :
                first = True
            if b == y:
                second = True
            if c == z:
                third = True

            if first and second and third:
                return True

        return first and second and third
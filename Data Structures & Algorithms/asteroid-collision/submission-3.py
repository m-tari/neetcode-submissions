class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue

            while stack and abs(a) > stack[-1] and stack[-1] > 0:
                stack.pop()

            if stack and abs(a) == stack[-1] and stack[-1] > 0:
                stack.pop()
                continue
            
            if not stack or stack[-1] < 0:
                stack.append(a)

        return stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for num in asteroids:
            if num > 0:
                stack.append(num)
                continue

            if stack and abs(num) == stack[-1] and stack[-1] > 0:
                stack.pop()
                continue

            while stack and abs(num) > stack[-1] and stack[-1] > 0:
                stack.pop()

            if not stack:
                stack.append(num)

        return stack
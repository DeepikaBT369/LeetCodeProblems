class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(speed):
            return sum((pile + speed - 1) // speed for pile in piles)  # ceiling division

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left
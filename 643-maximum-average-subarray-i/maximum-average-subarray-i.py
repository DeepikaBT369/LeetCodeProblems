class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right-k]
            best_sum = max(window_sum, best_sum)

        return best_sum/k
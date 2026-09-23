class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = threshold * k          # compare sums directly, avoid repeated division
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target_sum else 0

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]
            if window_sum >= target_sum:
                count += 1

        return count
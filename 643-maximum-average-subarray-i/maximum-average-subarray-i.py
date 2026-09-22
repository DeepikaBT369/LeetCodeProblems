class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k]) 
        # this is slicing the window and having the sum of them all
        # in the above we already built it from 0 till 3, that are 4 numbers

        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right-k]
            # best_sum = max(window_sum, best_sum)
            if best_sum< window_sum:
                best_sum = window_sum


        return best_sum/k
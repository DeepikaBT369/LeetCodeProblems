class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left = 0
        window_sum = 0
        count = 0
        for right in range(len(arr)):
            window_sum += arr[right]
            window_length = right-left+1
        
            if window_length>k:
                window_sum -= arr[left]
                left+=1
                window_length = right-left+1
               
            if window_length == k:
                if window_sum >= k*threshold:
                    count+=1
        return count
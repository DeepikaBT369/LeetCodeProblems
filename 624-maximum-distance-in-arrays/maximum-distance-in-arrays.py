from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize min and max using the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        # Loop through arrays starting from the second one
        for i in range(1, len(arrays)):
            # Update max_distance using current array and previous min/max
            max_distance = max(max_distance,
                               abs(arrays[i][-1] - min_val),  # current max - smallest so far
                               abs(max_val - arrays[i][0]))   # largest so far - current min
            
            # Update min_val and max_val for next iterations
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return max_distance
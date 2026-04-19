from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # cheapest toy so far
        max_profit = 0            # most candy
        
        for price in prices:
            if price < min_price:
                min_price = price  # found cheaper toy
            else:
                profit = price - min_price  # candy if we sell now
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
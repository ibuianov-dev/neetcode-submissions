class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_pointer = 0
        max_profit = 0
        
        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[day_pointer]
            if current_profit < 0:
                day_pointer = i
            else:
                max_profit = max(max_profit, current_profit)

        return max_profit
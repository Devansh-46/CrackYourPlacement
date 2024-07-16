class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = float('inf')
        max_profit = 0

        for price in prices:
            if min_value > price:
                min_value = price
            else:
                profit += price - min_value
                min_value = price


        return profit
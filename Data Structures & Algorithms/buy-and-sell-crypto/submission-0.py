class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0

        for price in prices:
            

            profit=price-min_buy

            max_profit=max(profit,max_profit)

            min_buy=min(price,min_buy)

        return max_profit
        
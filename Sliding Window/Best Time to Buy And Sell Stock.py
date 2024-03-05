class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        ans = 0

        for price in prices:
            if price < lowest:
                lowest = price
            elif price - lowest > ans:
                ans = price - lowest

        return ans
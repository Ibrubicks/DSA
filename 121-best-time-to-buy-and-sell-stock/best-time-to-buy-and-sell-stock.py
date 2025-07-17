class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        prof=0
        for price in prices:
            if price < buy:
                buy = price
            else:
                prof = max(prof,price-buy)
        return prof
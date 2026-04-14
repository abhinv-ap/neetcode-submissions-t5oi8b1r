class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy=prices[0]
        maxp=0
        for i in prices:
            maxp=max(maxp,i-minbuy)
            minbuy=min(minbuy,i)
        return maxp
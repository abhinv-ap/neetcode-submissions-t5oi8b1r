class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)
        curr=prices[0]
        for i in range(1,n):
            profit=max(profit,prices[i]-curr)
            if prices[i]<curr:
                curr=prices[i]

        return profit


        
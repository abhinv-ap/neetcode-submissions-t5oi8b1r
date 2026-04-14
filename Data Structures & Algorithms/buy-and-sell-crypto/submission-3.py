class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        now=prices[0]
        for i in range (1,len(prices)):
            profit=prices[i]-now
            if profit<0:
                now = prices[i]
            res=max(res,profit)
        return res


        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        c=prices[0]
        for i in prices:
            profit=profit+max(0,i-c)
            c=i
        return profit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profit=0
        curr=prices[0]
        n=len(prices)
        for i in range(1,n):
            if prices[i]<curr:
                curr=prices[i]
            else:
                profit+=(-curr+prices[i])
                curr=prices[i]
        return profit




        
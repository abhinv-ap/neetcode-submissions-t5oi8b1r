class Solution:
    def arrangeCoins(self, n: int) -> int:
        minn=1
        maxx=n
        res=1
        while minn<=maxx:
            mid=(maxx+minn)//2
            summ=(mid*(mid+1))//2
            if summ==n:
                return mid
            if summ > n:
                maxx=mid-1
            else:
                res=max(mid,res)
                minn=mid+1          
        return res

        
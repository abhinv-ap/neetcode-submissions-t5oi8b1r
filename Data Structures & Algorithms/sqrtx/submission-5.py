class Solution:
    def mySqrt(self, x: int) -> int:
        ans=int(x/2)
        while(True):
            if ans*ans==x:
                return ans
            elif ans*ans>x:
                ans=int(ans/2)
            else:
                if ans*ans<x and (ans+1)*(ans+1)>x:
                    return ans
                else:
                    ans+=1
        
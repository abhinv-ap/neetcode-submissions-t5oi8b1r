class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        minn=0
        maxx=num
        while minn <= maxx:
            mid=(minn+maxx)//2

            if mid*mid == num:
                return True
            if mid*mid>num:
                maxx=mid-1
            if mid*mid<num:
                minn=mid+1
        
        return False
            
        
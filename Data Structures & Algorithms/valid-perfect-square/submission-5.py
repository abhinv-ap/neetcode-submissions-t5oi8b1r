class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        minn=1
        maxx=math.ceil(num/2)
        while minn <= maxx:
            mid=(minn+maxx)//2

            if mid*mid == num:
                return True
            if mid*mid>num:
                maxx=mid-1
            if mid*mid<num:
                minn=mid+1
        
        return False
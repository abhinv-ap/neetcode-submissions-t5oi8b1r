class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        h = mountainArr.length() - 1
        l=0
        peak=h+1
        while True :
            m=(l+h)//2
            val=mountainArr.get(m)
            if mountainArr.get(m-1)<val<mountainArr.get(m+1):
                l=m+1
            elif mountainArr.get(m-1)>val>mountainArr.get(m+1):
                h=m-1
            else:
                peak=m
                break
        l=0
        h=peak     
        while(l<=h):
            m=(l+h)//2
            val=mountainArr.get(m)
            if val == target :
                return m
            elif val > target:
                h=m-1
            else:
                l=m+1
        l = peak
        h=mountainArr.length() - 1
        while(l<=h):
            m=(l+h)//2
            val=mountainArr.get(m)
            if val == target :
                return m
            elif val > target:
                l=m+1
            else:
                h=m-1
        return -1



        
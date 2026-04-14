class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ml=height[0]
        mr=height[-1]
        water=0
        while l<r:
            if ml<mr:
                l+=1
                water+=max(0,ml-height[l])
                ml=max(ml,height[l])
            else:
                r-=1
                water+=max(0,mr-height[r])
                mr=max(mr,height[r])
        return water





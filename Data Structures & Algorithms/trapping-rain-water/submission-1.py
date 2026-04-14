class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        while(len(height)>1):
            r=0
            while(r<len(height) and height[r]<1):
                r+=1
            height=height[r:]
            while height and height[-1]<=0:
                height.pop()
            for i in height:
                if i<1:
                    water+=1
            for i in range(len(height)):
                height[i] -= 1.

        return water
        
        
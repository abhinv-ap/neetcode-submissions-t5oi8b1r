# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Phase 1: Find the peak index
        l, h = 0, n - 1
        while l < h:
            m = (l + h) // 2
            # We only need 2 API calls here. No out-of-bounds risk since m < h.
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1  # The mountain is going up, peak is to the right
            else:
                h = m      # The mountain is going down, peak is m or to the left
        
        peak = l  # l and h converge exactly at the peak
        
        # Phase 2: Binary search on the ascending left side
        l, h = 0, peak
        while l <= h:
            m = (l + h) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                h = m - 1
                
        # Phase 3: Binary search on the descending right side
        l, h = peak + 1, n - 1
        while l <= h:
            m = (l + h) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                # Since the right side descends, if our value is too big, 
                # the smaller target must be further down to the right.
                l = m + 1
            else:
                h = m - 1
                
        # If not found on either side
        return -1
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window=set()
        l=0
        h=0

        while(h<len(nums)):
            if h-l <= k:
                if nums[h] in window:
                    return True
                window.add(nums[h])
                h+=1
            else:
                window.remove(nums[l])
                l+=1
        
        return False
        
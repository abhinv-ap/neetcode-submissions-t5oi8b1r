class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a=set()
        size=k
        l,r=0,0
        while r <len(nums):
            if r-l <= k:
                if nums[r] in a:
                    return True
                else:
                    a.add(nums[r])
                    r+=1
            else:
                a.remove(nums[l])
                l+=1
    
                
                
        
        return False


        
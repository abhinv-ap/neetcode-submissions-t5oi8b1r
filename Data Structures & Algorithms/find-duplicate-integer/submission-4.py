class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        while c<n:
            if nums[c]==c+1:
                c+=1
            else:
                if nums[c]==nums[nums[c]-1]:
                    return nums[c]
                else:
                    target = nums[c] - 1
                    nums[c], nums[target] = nums[target], nums[c]
                
        return -1
            
        

            


        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        c=0
        r=len(nums)-1
        while c<=r:
            if nums[c]==0:
                nums[c],nums[l]=nums[l],nums[c]
                l+=1
                c+=1
            elif nums[c]==2:
                nums[c],nums[r]=nums[r],nums[c]
                r-=1
            else:
                c+=1


 
       

        
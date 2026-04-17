class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h=len(nums)-1
        l=0
        m=0

        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            
            elif nums[m]==2:
                nums[h],nums[m]=nums[m],nums[h]
                h-=1
            else:
                m+=1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if 0<nums[i]<=len(nums) and nums[i]!= nums[nums[i]-1] and nums[i]!=i+1:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        j=0
        print(nums)
        while(j<len(nums) and nums[j]==j+1):
            j+=1
        return j+1 if j>0 else 1

                

        
        
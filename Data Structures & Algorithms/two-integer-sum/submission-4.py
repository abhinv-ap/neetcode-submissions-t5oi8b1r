class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i in range(len(nums)):
            if (-nums[i]+target) in dic:
                return [dic[(-nums[i]+target)],i]
            dic[nums[i]] =i 
                
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            req_no=target-nums[i]
            if req_no in dic:
                return [dic.get(req_no),i]
            else:
                dic[nums[i]]=i
        
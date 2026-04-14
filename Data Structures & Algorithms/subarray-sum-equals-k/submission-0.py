class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        pre={0:1}
        count=0

        for i in range(len(nums)):
            count+=nums[i]
            if count-k in pre:
                res+=pre[count-k]
            pre[count]=pre.get(count,0)+1
        return res
            




        
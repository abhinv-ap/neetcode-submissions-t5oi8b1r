class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pre=[0 for i in range (len(nums))]

        for i in range(len(nums)):
            pre[i] = pre[i-1] + nums[i] if i>0 else nums[i]

        counter=0
        dic={0:1}
        for i in pre:
            diff=i-k
            counter += dic.get(diff,0)
            dic[i]=1+dic.get(i,0)

        return counter

        


        
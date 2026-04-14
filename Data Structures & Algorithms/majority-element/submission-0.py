class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=defaultdict(int)
        count=0
        for i in nums:
            res[i] = res[i] + 1
        

        for i in res:
            if res[i] > count:
                max=i
                count=res[i]

        return max
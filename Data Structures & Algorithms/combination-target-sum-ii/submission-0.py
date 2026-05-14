class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        nums.sort()
        curr=[]
        res=[]
        def dfs(i):
            if sum(curr)==target:
                res.append(curr.copy())
                return
            
            if i>len(nums)-1 or sum(curr)>target:
                return

            curr.append(nums[i])
            dfs(i+1)
            while (i<len(nums)-1 and nums[i]==nums[i+1]):
                i+=1
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res
        
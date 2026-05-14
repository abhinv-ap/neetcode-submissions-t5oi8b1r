class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur_com=[]
        res=[]

        def dfs(i):
            if sum(cur_com)==target:
                res.append(cur_com.copy())
                return
            
            if i >= len(nums) or sum(cur_com)>target :
                return

            cur_com.append(nums[i])
            dfs(i)
            cur_com.pop()
            dfs(i+1)
        
    

        dfs(0)
        return res
            



            


        
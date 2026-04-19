class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref=min(strs,key=len)
        
        for i in range(len(ref)):
            for p in range(len(strs)):
                if strs[p][i]!=ref[i]:
                    return ref[:i]      

        return ref


        
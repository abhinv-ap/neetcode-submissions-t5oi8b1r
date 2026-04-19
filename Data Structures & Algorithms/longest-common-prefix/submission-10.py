class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref=strs[0]
        for i in strs:
            if len(i)<len(ref):
                ref=i
        
        for i in range(len(ref)):
            for p in range(len(strs)):
                if strs[p][i]!=ref[i]:
                    return ref[:i]      

        return ref


        
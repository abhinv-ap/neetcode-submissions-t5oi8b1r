class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref=strs[0]
        for i in strs:
            if len(i)<len(ref):
                ref=i
        j=0
        for i in range(len(ref)):
            curr=ref[j]
            for p in range(len(strs)):
                if strs[p][j]!=ref[j]:
                    return ref[:j]      
            j+=1

        return ref


        
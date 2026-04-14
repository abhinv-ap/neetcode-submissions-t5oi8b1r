class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]

        for i in range(1,len(strs)):
            j=0
            while j < min(len(p),len(strs[i])):
                if p[j] == strs[i][j]:
                    j=j+1
                else:
                    break
            p=p[:j]
                
        return p

        
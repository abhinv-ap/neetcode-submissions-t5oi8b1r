class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1={}
        for i in range(len(s1)):
            c1[s1[i]]=1+c1.get(s1[i],0)
        
        for r in range(len(s2)-len(s1)+1):
            c2={}
            for j in range(r,r+len(s1)):
                c2[s2[j]] = 1 + c2.get(s2[j], 0)
            if c1==c2:
                return True
        return False

        
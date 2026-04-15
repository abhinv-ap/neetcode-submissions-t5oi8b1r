class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1={}
        counter2={}

        for i in range(len(s1)):
            counter1[s1[i]]=counter1.get(s1[i],0)+1
        l=0
        for i in range(len(s2)):
            counter2[s2[i]]=counter2.get(s2[i],0)+1

            while i-l+1>len(s1):
                counter2[s2[l]]=counter2.get(s2[l])-1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                l=l+1
            
            if counter1==counter2:
                return True
        
        return False

        
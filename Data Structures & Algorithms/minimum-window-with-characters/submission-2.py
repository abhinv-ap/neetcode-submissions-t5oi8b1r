class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ''
        count1={}

        for c in range(len(t)):
            count1[t[c]]=1+count1.get(t[c],0)
        need = len(count1)
        have=0
        count2={}
        length=float('inf')
        l=0
        al=None
        ah=None

        for r in range(len(s)):

            count2[s[r]]=1+count2.get(s[r],0)

            if count2.get(s[r],0) == count1.get(s[r],-1):
                have +=1

            while have == need:
                if r - l + 1 < length:
                    length = r-l+1
                    al=l
                    ah=r
                
                if count2.get(s[l],0) == count1.get(s[l],-1):
                    have -=1

                count2[s[l]] = count2.get(s[l])-1

                l=l+1

        
        return s[al:ah+1] if al is not None else ''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        window=set()
        m=1
        maxs=0
        for i in range(len(s)):
            if s[i] in window:
                while(s[l]!=s[i]):
                    window.remove(s[l])
                    m=m-1
                    l=l+1
                window.remove(s[l])
                m=m-1
                l=l+1
                
            window.add(s[i])
            m+=1
            maxs=max(maxs,m)
        maxs-=1
        maxs=max(maxs,0)
        return maxs


        
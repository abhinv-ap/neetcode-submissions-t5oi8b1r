class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        l=0
        m=0
        res=0
        for i in range(len(s)):
            if s[i] in window:
                while s[i] in window:
                    window.remove(s[l])
                    l+=1
                    m-=1
            window.add(s[i])
            m+=1
            res=max(res,m)
        return res



        
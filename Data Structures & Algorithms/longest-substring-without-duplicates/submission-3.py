class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        window=set()
        maxs=0
        for i in range(len(s)):
            while(s[i] in window):
                window.remove(s[l])
                l=l+1
                
            window.add(s[i])
            maxs=max(maxs,i-l+1)
    
        return maxs


        
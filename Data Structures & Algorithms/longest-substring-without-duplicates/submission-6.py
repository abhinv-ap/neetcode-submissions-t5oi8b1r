class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        h=0
        maxx=0
        window=set()
        while h<len(s):
            if s[h] in window:
                window.remove(s[l])
                l+=1
            else:
                window.add(s[h])
                h+=1
                maxx=max(maxx,h-l+1)
        
        return max(maxx-1,0)

        
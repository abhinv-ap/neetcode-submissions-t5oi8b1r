class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = list(s)
        b = list(t)
        for i in a:
            for j in range (len(b)):
                if b[j]==i:
                    b.pop(j)
                    break
        if not b :
            return True
        else:
            return False

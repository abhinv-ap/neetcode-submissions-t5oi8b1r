class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastword=s.split()[-1]
        return len(lastword)
        
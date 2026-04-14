class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a,b=0,0
        new=''
        while(a<len(word1) and b<len(word2)):
            new=new+word1[a]+word2[b]
            a+=1
            b+=1

        if(a>len(word1)-1):
            new=new+word2[a:]
        else:
            new=new+word1[a:]
        
        return new
        
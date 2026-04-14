class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=''
        for i in strs:
            a=str(len(i))
            a=a+"#"+i
            enc=enc+a
        print(enc)
        return(enc)

    def decode(self, s: str) -> List[str]:
        dec=[]
        st=s
        i=0
        while(i<len(s)):
            j=i
            while(st[j]!="#"):
                j+=1
            a=int(st[i:j])
            i=j+1
            dec.append(st[i:i+a])
            i=i+a
        return dec
    



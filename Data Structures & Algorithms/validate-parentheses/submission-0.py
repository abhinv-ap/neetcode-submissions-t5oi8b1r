class Solution:
    def isValid(self, s: str) -> bool:
        ctp={ ')':'(' ,']':'[' ,'}':'{' }
        stak=[]
        for i in s:
            if i in ctp :
                if not stak or ctp[i] != stak[-1]:
                    return False
                else:
                    stak.pop()
                
            else:
                stak.append(i)

        return not stak
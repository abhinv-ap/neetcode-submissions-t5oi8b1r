class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter={5:0,10:0,20:0}
        for i in bills:
            counter[i] = 1+counter.get(i,0)
            change=i-5
            if change:
                if change==15:
                    if counter[10] and counter[5]:
                        counter[10] = counter.get(10)-1
                        counter[5] = counter.get(5)-1
                    
                    else:
                        if counter[5]>=3:
                            counter[5] = counter.get(5)-3
                        else:
                            return False
                else:
                    if counter[5]>=1:
                            counter[5] = counter.get(5)-1
                    else:
                            return False
        
        return True






        
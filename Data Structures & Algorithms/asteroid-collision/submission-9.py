class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for i in asteroids:
            if not res:
                res.append(i)
                continue
            if i < 0 and res[-1]>0:
                if -i==res[-1]:
                    res.pop()
                    continue
                elif -i<res[-1]:
                    continue
                else:
                    while(res and res[-1]>0 and -i>res[-1]):
                        res.pop()
                    if(res and res[-1]==-i):
                        res.pop()
                        continue
                if not res or res[-1]<0:
                    res.append(i)
            else:
                res.append(i)
        return res


                    
                


        
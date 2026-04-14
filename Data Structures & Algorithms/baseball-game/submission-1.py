class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i =="+":
                res.append(res[-2]+res[-1])
            elif i =='C':
                res.pop()
            elif i=='D':
                res.append(2*int(res[-1]))
            else:
                res.append(int(i))
        return sum(res)

        
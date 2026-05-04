class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new=intervals
        new.sort()
        stack=[]
        for i in new:
            if not stack:
                stack.append(i)
                continue
            if stack[-1][1]>=i[0]:
                new=[stack[-1][0],max(i[1],stack[-1][1])]
                stack.pop()
                stack.append(new)
            else:
                stack.append(i)
        
        return stack
        
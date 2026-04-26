class Solution:
    def isValid(self, s: str) -> bool:
        cto={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i not in cto:
                stack.append(i)
            else:
                if not stack:
                    return False
                if cto[i]!=stack[-1] :
                    return False
                else:
                    stack.pop()

        if stack:
            return False
        return True
    
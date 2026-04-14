class Solution:
    def simplifyPath(self, path: str) -> str:
        words=path.split('/')
        print(words)
        stack=[]
        c='/'
        for i in words:
            if stack and i =='..' :
                stack.pop()
            elif i!=''and i!='..' and i!='.':
                stack.append(i)
        print(stack)
        return '/'+c.join(stack)
        

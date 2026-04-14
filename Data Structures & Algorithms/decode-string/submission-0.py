class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            temp=''
            k=''
            if i==']':
                while(stack[-1]!='['):
                    temp = stack.pop()+temp     
                stack.pop()
                while(stack and stack[-1].isdigit()):
                    k=stack.pop()+k
                temp=temp*int(k)
                for i in temp:
                    stack.append(i)
            else:
                stack.append(i)
        print(stack)
        return "".join(stack)
        
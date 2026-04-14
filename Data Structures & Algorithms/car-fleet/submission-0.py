class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        stack=[]
        for i in range(len(position)):
            time=(target-cars[i][0])/cars[i][1]

            if not stack or time>stack[-1]:
                stack.append(time)

        return(len(stack))


        
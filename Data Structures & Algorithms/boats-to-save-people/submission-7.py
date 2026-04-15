class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        l=0
        r=len(people)-1
        while l<=r:
            a=people[r]
            capacity=limit-a
            r-=1
            if people[l]<= capacity:
                l+=1
            count+=1


        
        return count
        

        
        
        
        
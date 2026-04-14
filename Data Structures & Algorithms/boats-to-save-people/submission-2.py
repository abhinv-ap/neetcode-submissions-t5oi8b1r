class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r=0,len(people)-1
        boats=0
        people.sort()
        while(l<=r ):
            diffrence=limit-people[r]
            r-=1
            boats+=1
            if (people[l]<=diffrence and l<=r ):
                l+=1
        return boats



        
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        boat = 0

        people.sort()

        l, r = 0, len(people)-1

        while l<=r:
            diff = limit - people[r]
            r-=1
            boat+=1
            if l<=r and diff>=people[l]:
                l+=1
            
            
        return boat

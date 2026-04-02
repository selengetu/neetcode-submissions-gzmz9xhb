class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        l , r = 0, len(people)-1
        boat = 0

        while l<=r:
            if limit - people[r] >= people[l]:
                l+=1
            boat+=1
            r-=1
        return boat


    
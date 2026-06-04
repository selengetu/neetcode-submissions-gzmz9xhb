class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l<=r:
            k = (r+l)//2

            total_hour = 0

            for p in piles:
                total_hour+= math.ceil(float(p)/k)
            
            if total_hour<=h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
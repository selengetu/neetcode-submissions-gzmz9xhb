class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        total = defaultdict(int)
        maxCount = 0
        res = 0
        for n in nums:
            total[n] +=1
            if total[n] > maxCount:
                maxCount = total[n]
                res = n
        return res
        
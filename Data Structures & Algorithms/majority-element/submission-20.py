class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        maxCount = 0
        maxNum = 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxCount:
                maxCount = count[n]
                maxNum = n
        return maxNum


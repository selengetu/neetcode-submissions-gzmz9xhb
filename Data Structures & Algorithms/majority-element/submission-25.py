class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        n = len(nums)
        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for k in count:
            if count[k] > n//2:
                return k
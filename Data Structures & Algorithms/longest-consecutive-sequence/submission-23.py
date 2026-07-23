class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq_set = set(nums)
        length = 1
        maxlength = 0
        for n in nums:
            
            if n-1 not in uniq_set:
                length = 1
                while n+length in uniq_set:
                    length+=1
            maxlength = max(length, maxlength)
        return maxlength
            

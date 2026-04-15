class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dup_num = set(nums)
        length = 0
        maxLength = 0
        for n in nums:
            if n-1 not in dup_num:
                length =1
                while n+length in dup_num:
                    length +=1
            maxLength = max(length, maxLength)
        return maxLength
        
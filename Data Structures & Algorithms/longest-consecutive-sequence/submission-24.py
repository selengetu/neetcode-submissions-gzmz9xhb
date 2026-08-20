class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq_number = set(nums)
        max_length = 0

        for n in nums:
            if n-1 not in uniq_number:
                length = 1
                while n+length in uniq_number:
                    length +=1
                max_length = max(max_length,length)
        return max_length
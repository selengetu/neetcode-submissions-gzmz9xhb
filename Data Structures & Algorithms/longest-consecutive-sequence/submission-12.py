class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq_num = set(nums)

        length = 0
        longest = 0

        for num in nums:
            if num-1 not in uniq_num:
                length = 1

                while num + length in uniq_num:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
                
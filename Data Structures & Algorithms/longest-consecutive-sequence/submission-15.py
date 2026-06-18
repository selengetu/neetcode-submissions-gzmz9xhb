class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        dedup = set(nums)
        length = 0
        longest = 0
        
        for n in nums:
            if n-1 not in dedup:
                length = 1
                while n+length in dedup:
                    length +=1
                longest = max(longest, length)
        return longest

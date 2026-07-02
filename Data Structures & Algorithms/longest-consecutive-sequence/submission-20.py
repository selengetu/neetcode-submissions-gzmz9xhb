class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq = set(nums)
        maxlength = 0

        for n in nums:
            if n-1 not in uniq:
                length = 1
                while n+length in uniq:
                    length +=1

                maxlength = max(maxlength, length)
        return maxlength
                
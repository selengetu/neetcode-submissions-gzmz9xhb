class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq = set(nums)
        length = 0
        
        maxlength = 0

        for num in nums:
            if num - 1 not in uniq:
                length = 1
                while (num + length) in uniq:
                    length +=1
                
                maxlength = max(length, maxlength)

        return maxlength